/* ==========================================================================
   Second Brain — frontend application (Phase 2)
   ========================================================================== */

const API = "/api";
const $ = (s) => document.querySelector(s);
const $$ = (s) => Array.from(document.querySelectorAll(s));

const TYPE_COLORS = {
  person: "#f472b6", project: "#22d3ee", technology: "#34d399",
  topic: "#a78bfa", skill: "#2dd4bf", goal: "#60a5fa",
  interest: "#fb923c", preference: "#e879f9", fact: "#f87171",
  location: "#4ade80", organization: "#38bdf8", concept: "#fbbf24",
  task: "#94a3b8", event: "#f472b6",
};

function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

async function api(path, opts = {}) {
  const res = await fetch(API + path, {
    headers: { "Content-Type": "application/json" },
    ...opts,
  });
  if (!res.ok) {
    let msg = res.statusText;
    try { msg = (await res.json()).detail || msg; } catch {}
    throw new Error(msg);
  }
  return res.json();
}

function toast(text) {
  const t = $("#toast");
  t.textContent = text;
  t.classList.add("show");
  clearTimeout(t._timer);
  t._timer = setTimeout(() => t.classList.remove("show"), 2600);
}

function badge(type) {
  return `<span class="badge ${esc(type)}">${esc(type)}</span>`;
}

function fmtTime(iso) {
  const d = new Date(iso);
  return d.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}
function fmtDay(iso) {
  const d = new Date(iso);
  return d.toLocaleDateString([], { weekday: "long", month: "long", day: "numeric", year: "numeric" });
}

let typeColors = TYPE_COLORS;

/* ==========================================================================
   Navigation
   ========================================================================== */
const VIEWS = ["dashboard", "chat", "graph", "browse", "memory", "search", "settings"];
let currentView = "dashboard";

function parseHash() {
  const raw = (location.hash || "").replace(/^#/, "");
  const parts = raw.split("/");
  return { view: parts[0] || "", extra: parts[1] || "" };
}

function setHash(view, extra) {
  const next = extra ? ("#" + view + "/" + extra) : ("#" + view);
  if (location.hash !== next) {
    try { history.replaceState(null, "", next); } catch {}
  }
}

function showView(name, opts = {}) {
  if (!VIEWS.includes(name)) name = "dashboard";
  currentView = name;
  VIEWS.forEach((v) => {
    const el = $("#view-" + v);
    if (el) el.classList.toggle("active", v === name);
  });
  $$(".nav-item").forEach((b) => b.classList.toggle("active", b.dataset.view === name));
  if (!opts.keepHash) setHash(name);
  if (name === "graph") requestAnimationFrame(() => { if (cy) cy.fit(undefined, 30); });
  if (name === "dashboard") loadDashboard();
  if (name === "memory") loadMemory();
  if (name === "browse") loadBrowse();
  if (name === "chat") scrollChat();
  if (name === "settings") { loadSettings(); loadBackupStatus(); }
}

function applyRoute() {
  const h = parseHash();
  if (h.view === "entity" && h.extra) {
    showView("graph", { keepHash: true });
    openEntity(h.extra);
    return;
  }
  if (h.view === "chat") {
    showView("chat", { keepHash: true });
    if (h.extra) openConversation(Number(h.extra));
    return;
  }
  if (VIEWS.includes(h.view)) showView(h.view, { keepHash: true });
}

window.addEventListener("hashchange", applyRoute);

$$(".nav-item").forEach((b) =>
  b.addEventListener("click", () => showView(b.dataset.view)));

/* ==========================================================================
   Status / health
   ========================================================================== */
async function refreshStatus() {
  try {
    const h = await api("/health");
    const dot = $(".status-dot");
    const txt = $(".status-text");
    if (h.ollama_available) {
      dot.className = "status-dot on";
      txt.textContent = "Ollama online";
    } else {
      dot.className = "status-dot off";
      txt.textContent = "Ollama offline (fallback)";
    }
    $("#model-line").textContent = `LLM: ${h.llm_model} · EMB: ${h.embedding_model}`;
  } catch {}
}

/* ==========================================================================
   Dashboard
   ========================================================================== */
async function loadDashboard() {
  const d = await api("/dashboard");
  const stats = [
    ["Entities", d.entities], ["Relationships", d.relationships],
    ["Memories", d.memories], ["Conversations", d.conversations],
    ["Technologies", d.by_type.technology || 0], ["Projects", d.by_type.project || 0],
    ["People", d.by_type.person || 0], ["Pinned", d.pinned],
  ];
  $("#stats-grid").innerHTML = stats
    .map(([l, n]) => `<div class="stat-card"><div class="stat-num">${n}</div><div class="stat-label">${l}</div></div>`)
    .join("");

  // Growth chart
  const max = Math.max(1, ...d.growth.map((g) => g.count));
  $("#growth-chart").innerHTML = d.growth.map((g) => `
    <div class="grow-bar" style="height:${Math.max(3, (g.count / max) * 100)}%">
      <span class="grow-tip">${g.date.slice(5)} · ${g.count}</span>
    </div>`).join("");

  // Type breakdown
  const types = Object.entries(d.by_type).sort((a, b) => b[1] - a[1]);
  const total = types.reduce((s, [, n]) => s + n, 0) || 1;
  $("#type-breakdown").innerHTML = types.length ? types.map(([t, n]) => `
    <div class="type-row">
      <span class="type-dot" style="background:${typeColors[t] || "#8899bb"}"></span>
      <span class="type-name">${esc(t)}</span>
      <span class="type-bar-track"><span class="type-bar-fill" style="width:${(n / total) * 100}%;background:${typeColors[t] || "#8899bb"}"></span></span>
      <span class="type-count">${n}</span>
    </div>`).join("") : `<p class="muted">No entities yet.</p>`;

  $("#recent-memories").innerHTML = d.recent.length
    ? d.recent.map((m) => `
        <div class="mem-item">
          <span class="mem-ico">${m.kind === "entity" ? "◆" : m.kind === "superseded" ? "⤫" : "⇄"}</span>
          <span class="mem-text">${esc(m.text)}</span>
          <span class="mem-time">${fmtTime(m.created_at)}</span>
        </div>`).join("")
    : `<p class="muted">No memories yet — start chatting.</p>`;

  $("#top-entities").innerHTML = d.most_connected.length
    ? d.most_connected.map((e) => `
        <div class="entity-mini" data-id="${e.id}">
          <span style="color:${typeColors[e.type] || "#fff"}">●</span>
          <span class="em-name">${esc(e.name)}</span>
          ${badge(e.type)}
          <span class="em-degree">${e.degree}</span>
        </div>`).join("")
    : `<p class="muted">Nothing yet.</p>`;
  $$("#top-entities .entity-mini").forEach((el) =>
    el.addEventListener("click", () => openEntity(el.dataset.id)));

  const banner = $("#demo-banner");
  if (banner) banner.style.display = d.has_demo_data ? "" : "none";
}

/* ==========================================================================
   Chat
   ========================================================================== */
let currentConversationId = null;

function scrollChat() {
  const s = $("#chat-scroll");
  s.scrollTop = s.scrollHeight;
}

function rememberChips(remembered) {
  if (!remembered || !remembered.length) return "";
  const parts = remembered.map((r) => {
    if (r.kind === "entity") {
      return `<span class="remembered-chip" data-id="${r.entity_id}">
        <span style="color:${typeColors[r.type] || "#fff"}">●</span> ${esc(r.name)}
        <span class="conf">${Math.round((r.confidence || 0.8) * 100)}%</span></span>`;
    }
    return `<span class="remembered-chip" data-id="${r.target_id || r.entity_id}">
      ${esc(r.source)} <span class="arrow">→</span> <span class="rel">${esc(r.relation)}</span> <span class="arrow">→</span> ${esc(r.target)}
      <span class="conf">${Math.round((r.confidence || 0.8) * 100)}%</span></span>`;
  }).join("");
  return `<div class="remembered-title">Memory updated</div>${parts}`;
}

function sourceChips(sources) {
  if (!sources || !sources.length) return "";
  return `<div class="remembered-title">Sources</div>` +
    sources.map((s) => `<span class="remembered-chip" data-id="${s.entity_id}">${esc(s.name)}${s.fact ? ` · <span class="conf">${esc(s.fact)}</span>` : ""}${s.snippet ? ` · <span class="conf">${esc(s.snippet)}</span>` : ""}</span>`).join("");
}

function attachChips(root) {
  if (!root) return;
  root.querySelectorAll(".remembered-chip").forEach((chip) =>
    chip.addEventListener("click", () => openEntity(chip.dataset.id)));
}

function appendMessage(role, content, opts = {}) {
  $("#chat-empty").style.display = "none";
  const wrap = document.createElement("div");
  wrap.className = "msg " + role;

  if (content) {
    const b = document.createElement("div");
    b.className = "msg-bubble";
    b.textContent = content;
    if (opts.status) {
      const st = document.createElement("span");
      st.className = "ans-status ans-" + opts.status;
      st.textContent = opts.status;
      b.prepend(st, document.createTextNode(" "));
    }
    wrap.appendChild(b);
  }

  if (opts.remembered && opts.remembered.length) {
    const box = document.createElement("div");
    box.className = "remembered-box";
    box.innerHTML = rememberChips(opts.remembered);
    wrap.appendChild(box);
    box.querySelectorAll(".remembered-chip").forEach((chip) =>
      chip.addEventListener("click", () => openEntity(chip.dataset.id)));
  }

  if (opts.superseded && opts.superseded.length) {
    const note = document.createElement("div");
    note.className = "superseded-note";
    note.textContent = "Superseded: " + opts.superseded.join(", ");
    wrap.appendChild(note);
  }

  if (opts.sources && opts.sources.length) {
    const src = document.createElement("div");
    src.className = "remembered-box";
    src.innerHTML = sourceChips(opts.sources);
    wrap.appendChild(src);
    attachChips(src);
  }

  const t = document.createElement("div");
  t.className = "msg-time";
  t.textContent = fmtTime(new Date().toISOString());
  wrap.appendChild(t);
  $("#chat-messages").appendChild(wrap);
  scrollChat();
}

function parseSseBuffer(buffer, onEvent) {
  const parts = buffer.split("\n\n");
  const rest = parts.pop();
  for (const block of parts) {
    let event = "message";
    const dataLines = [];
    for (const line of block.split("\n")) {
      if (line.startsWith("event:")) event = line.slice(6).trim();
      else if (line.startsWith("data:")) dataLines.push(line.slice(5).trim());
    }
    if (!dataLines.length) continue;
    try { onEvent(event, JSON.parse(dataLines.join("\n"))); } catch {}
  }
  return rest;
}

async function sendChat() {
  const input = $("#chat-input");
  const content = input.value.trim();
  if (!content) return;
  input.value = "";
  input.style.height = "auto";
  appendMessage("user", content);
  $("#chat-send").disabled = true;

  const wrap = document.createElement("div");
  wrap.className = "msg assistant";
  const bubble = document.createElement("div");
  bubble.className = "msg-bubble streaming";
  wrap.appendChild(bubble);
  $("#chat-empty").style.display = "none";
  $("#chat-messages").appendChild(wrap);
  scrollChat();

  let reply = "";
  let remembered = [];
  let superseded = [];
  let status = "";
  let sources = [];
  let usedFallback = false;

  const finish = (r = {}) => {
    reply = r.reply != null ? r.reply : reply;
    remembered = r.remembered || remembered;
    superseded = r.superseded || superseded;
    status = r.status || status;
    sources = r.sources || sources;
    if (r.used_fallback) usedFallback = true;
    r.used_fallback = usedFallback || r.used_fallback;
    if (r.conversation_id) currentConversationId = r.conversation_id;
    bubble.classList.remove("streaming");
    bubble.textContent = reply;
    if (status) {
      const st = document.createElement("span");
      st.className = "ans-status ans-" + status;
      st.textContent = status === "answered" ? "known" : status;
      bubble.prepend(st, document.createTextNode(" "));
    }
    if (remembered && remembered.length) {
      const box = document.createElement("div");
      box.className = "remembered-box";
      box.innerHTML = rememberChips(remembered);
      wrap.appendChild(box);
      box.querySelectorAll(".remembered-chip").forEach((chip) =>
        chip.addEventListener("click", () => openEntity(chip.dataset.id)));
    }
    if (superseded && superseded.length) {
      const note = document.createElement("div");
      note.className = "superseded-note";
      note.textContent = "Superseded: " + superseded.join(", ");
      wrap.appendChild(note);
    }
    if (sources && sources.length) {
      const src = document.createElement("div");
      src.className = "remembered-box";
      src.innerHTML = sourceChips(sources);
      wrap.appendChild(src);
      attachChips(src);
    }
    const t = document.createElement("div");
    t.className = "msg-time";
    t.textContent = fmtTime(new Date().toISOString());
    wrap.appendChild(t);
    if (r.used_fallback) {
      const chip = document.createElement("span");
      chip.className = "offline-chip";
      chip.textContent = "offline extractor";
      bubble.appendChild(document.createTextNode(" "));
      bubble.appendChild(chip);
    }
    if (remembered && remembered.length) { loadDashboard(); buildGraph(); }
    if (r.is_command || (remembered && remembered.length)) loadDashboard();
    loadConversations();
    scrollChat();
  };

  try {
    const res = await fetch(API + "/chat/stream", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content, conversation_id: currentConversationId }),
    });
    if (!res.ok || !res.body) {
      const r = await api("/chat", {
        method: "POST",
        body: JSON.stringify({ content, conversation_id: currentConversationId }),
      });
      finish(r);
      return;
    }
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buf = "";
    let donePayload = null;
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      buf += decoder.decode(value, { stream: true });
      buf = parseSseBuffer(buf, (event, data) => {
        if (event === "meta" && data.conversation_id) currentConversationId = data.conversation_id;
        if (event === "token" && data.text) {
          reply += data.text;
          bubble.textContent = reply;
          scrollChat();
        }
        if (event === "memory") {
          remembered = data.remembered || [];
          superseded = data.superseded || [];
          if (data.used_fallback) usedFallback = true;
        }
        if (event === "status") status = data.status || status;
        if (event === "sources") sources = data.sources || [];
        if (event === "done") donePayload = data;
      });
    }
    finish(donePayload || { reply, remembered, superseded, status, sources });
  } catch (e) {
    try {
      const r = await api("/chat", {
        method: "POST",
        body: JSON.stringify({ content, conversation_id: currentConversationId }),
      });
      finish(r);
    } catch (err) {
      bubble.classList.remove("streaming");
      bubble.textContent = "⚠ " + err.message;
    }
  } finally {
    $("#chat-send").disabled = false;
    scrollChat();
  }
}

$("#chat-send").addEventListener("click", sendChat);
$("#chat-input").addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); sendChat(); }
});
$("#chat-input").addEventListener("input", (e) => {
  e.target.style.height = "auto";
  e.target.style.height = Math.min(e.target.scrollHeight, 140) + "px";
});

$("#chat-new").addEventListener("click", async () => {
  const r = await api("/conversations/new", { method: "POST" });
  currentConversationId = r.conversation_id;
  setHash("chat", r.conversation_id);
  $("#chat-messages").innerHTML = "";
  $("#chat-empty").style.display = "";
  toast("Started a new conversation");
  loadConversations();
});

async function loadConversations() {
  const list = $("#conv-list");
  if (!list) return;
  const q = ($("#conv-search") && $("#conv-search").value.trim()) || "";
  try {
    const convs = await api("/conversations" + (q ? ("?q=" + encodeURIComponent(q)) : ""));
    if (!convs.length) {
      list.innerHTML = `<p class="muted">${q ? "No conversations match." : "No conversations yet."}</p>`;
      return;
    }
    list.innerHTML = convs.map((c) => `
      <div class="conv-item ${c.id === currentConversationId ? "active" : ""}" data-id="${c.id}">
        <div class="conv-title" data-id="${c.id}" title="Double-click to rename">${esc(c.title || "(untitled)")}</div>
        <div class="conv-preview">${esc(c.preview || "")}</div>
        <button class="rel-del conv-del" data-id="${c.id}" title="Delete conversation">✕</button>
      </div>`).join("");
    list.querySelectorAll(".conv-item").forEach((el) =>
      el.addEventListener("click", (ev) => {
        if (ev.target.closest(".conv-del") || ev.target.closest(".conv-title")) return;
        openConversation(Number(el.dataset.id));
      }));
    list.querySelectorAll(".conv-title").forEach((el) =>
      el.addEventListener("dblclick", (ev) => {
        ev.stopPropagation();
        renameConversation(Number(el.dataset.id), el);
      }));
    list.querySelectorAll(".conv-del").forEach((btn) =>
      btn.addEventListener("click", async (ev) => {
        ev.stopPropagation();
        if (!confirm("Delete this conversation? Long-term memories stay.")) return;
        const r = await api("/conversations/" + btn.dataset.id, { method: "DELETE" });
        if (currentConversationId === Number(btn.dataset.id)) {
          currentConversationId = r.conversation_id || null;
          $("#chat-messages").innerHTML = "";
          $("#chat-empty").style.display = "";
        }
        loadConversations();
      }));
    const src = $("#sf-source");
    if (src && !q) {
      const cur = src.value;
      src.innerHTML = `<option value="">Any source</option>` +
        convs.map((c) => `<option value="${c.id}">${esc(c.title || "Conversation " + c.id)}</option>`).join("");
      src.value = cur;
    }
  } catch {}
}

if ($("#conv-search")) {
  let convSearchTimer = null;
  $("#conv-search").addEventListener("input", () => {
    clearTimeout(convSearchTimer);
    convSearchTimer = setTimeout(loadConversations, 180);
  });
  $("#conv-search").addEventListener("keydown", (e) => {
    if (e.key === "Escape") { e.target.value = ""; loadConversations(); }
  });
}

async function renameConversation(id, el) {
  const current = el.textContent.trim();
  el.contentEditable = "true";
  el.focus();
  const range = document.createRange();
  range.selectNodeContents(el);
  const sel = window.getSelection();
  sel.removeAllRanges();
  sel.addRange(range);
  const done = async () => {
    el.contentEditable = "false";
    el.removeEventListener("blur", done);
    const title = el.textContent.trim().slice(0, 80);
    if (!title || title === current) { el.textContent = current; return; }
    await api("/conversations/" + id, { method: "PATCH", body: JSON.stringify({ title }) });
    loadConversations();
  };
  el.addEventListener("blur", done);
  el.addEventListener("keydown", (e) => {
    if (e.key === "Enter") { e.preventDefault(); el.blur(); }
    if (e.key === "Escape") { el.textContent = current; el.blur(); }
  }, { once: true });
}

async function openConversation(id) {
  currentConversationId = id;
  setHash("chat", id);
  $("#chat-messages").innerHTML = "";
  $("#chat-empty").style.display = "";
  const msgs = await api(`/conversations/${id}/messages`);
  msgs.forEach((m) => {
    if (m.role === "user") appendMessage("user", m.content);
    else appendMessage("assistant", m.content, {
      remembered: m.remembered, kind: m.kind, status: m.status,
      superseded: m.superseded, sources: m.sources,
    });
  });
  loadConversations();
}

async function loadChatHistory() {
  const convs = await api("/conversations");
  if (!convs.length) { loadConversations(); return; }
  currentConversationId = convs[0].id;
  await openConversation(convs[0].id);
}

/* ==========================================================================
   Knowledge Graph
   ========================================================================== */
let cy;
let graphNodes = [];

function initGraph() {
  cy = cytoscape({
    container: document.getElementById("cy"),
    style: [
      { selector: "node",
        style: {
          "background-color": (el) => typeColors[el.data("type")] || "#8899bb",
          "label": "data(label)",
          "color": "#e7ecf5",
          "font-size": 11,
          "text-valign": "center",
          "text-halign": "center",
          "text-wrap": "wrap",
          "text-max-width": 80,
          "width": (el) => el.data("important") ? 22 : 16,
          "height": (el) => el.data("important") ? 22 : 16,
          "border-width": (el) => el.data("pinned") ? 3 : 1.5,
          "border-color": (el) => el.data("pinned") ? "#fbbf24" : "#0a0e1a",
          "text-outline-width": 2, "text-outline-color": "#0a0e1a",
        } },
      { selector: "node:selected",
        style: { "border-width": 3, "border-color": "#ffffff" } },
      { selector: "node.dim", style: { opacity: 0.12 } },
      { selector: "node.superseded", style: { opacity: 0.3, "background-color": "#64748b" } },
      { selector: "edge",
        style: {
          "width": 1.4,
          "line-color": "rgba(140,155,190,0.35)",
          "target-arrow-color": "rgba(140,155,190,0.5)",
          "target-arrow-shape": "triangle",
          "curve-style": "bezier",
          "label": "data(relation)",
          "font-size": 8.5,
          "color": "rgba(170,185,215,0.75)",
          "text-rotation": "autorotate",
          "text-background-color": "#0a0e1a",
          "text-background-opacity": 0.7,
          "text-background-padding": 2,
        } },
      { selector: "edge.dim", style: { opacity: 0.05 } },
      { selector: "edge.superseded", style: { "line-style": "dashed", "line-color": "rgba(100,116,139,0.4)" } },
      { selector: "edge.highlight", style: { "line-color": "#22d3ee", "width": 2.2 } },
      { selector: "node.highlight", style: { "border-width": 2.5, "border-color": "#22d3ee" } },
    ],
    layout: {
      name: "cose",
      animate: true,
      animationDuration: 600,
      nodeRepulsion: () => 9000,
      idealEdgeLength: () => 90,
      edgeElasticity: () => 120,
      gravity: 0.25,
      numIter: 1500,
      padding: 40,
    },
    wheelSensitivity: 0.25,
  });

  cy.on("tap", "node", (e) => {
    const id = String(e.target.id());
    lastFocusedId = id;
    pathEnds = pathEnds.filter((x) => x !== id).concat([id]).slice(-2);
    openEntity(id);
  });
  cy.on("dbltap", "node", (e) => {
    lastFocusedId = String(e.target.id());
    expandSelectedNeighborhood();
  });
  cy.on("tap", (e) => { if (e.target === cy) closeEntity(); });

  cy.on("mouseover", "node", (e) => {
    const n = e.target;
    cy.elements().addClass("dim");
    n.removeClass("dim");
    n.neighborhood().removeClass("dim").addClass("highlight");
    n.addClass("highlight");
  });
  cy.on("mouseout", "node", () => cy.elements().removeClass("dim").removeClass("highlight"));
}

function buildLegend() {
  const types = [...new Set(graphNodes.map((n) => n.type))].sort();
  $("#graph-legend").innerHTML = types.map((t) => `
    <div class="legend-row" data-type="${esc(t)}">
      <span class="legend-dot" style="background:${typeColors[t] || "#8899bb"}"></span>
      ${esc(t)}
    </div>`).join("");
  $$(".legend-row").forEach((r) =>
    r.addEventListener("click", () => {
      r.classList.toggle("off");
      applyTypeFilter();
    }));
}

const hiddenTypes = new Set();
function applyTypeFilter() {
  $$(".legend-row").forEach((r) => {
    if (r.classList.contains("off")) hiddenTypes.add(r.dataset.type);
    else hiddenTypes.delete(r.dataset.type);
  });
  applyConnectedFilter();
}

async function buildGraph(opts = {}) {
  const aroundEl = $("#gf-around-me");
  let focus = opts.focus;
  if (!focus) focus = (aroundEl && aroundEl.checked) ? "user" : "auto";
  const g = await api("/graph?focus=" + encodeURIComponent(focus) + "&depth=2");
  graphNodes = g.nodes;
  typeColors = g.type_colors || TYPE_COLORS;
  if (aroundEl && g.focus === "user") aroundEl.checked = true;
  if (g.truncated && $("#gf-layout") && $("#gf-layout").value === "cose") {
    $("#gf-layout").value = "breadthfirst";
  }
  const nodes = g.nodes.map((n) => ({ data: { id: n.id, label: n.label, type: n.type, description: n.description, pinned: n.pinned, important: n.important, status: n.status } }));
  const edges = g.edges.map((e) => ({ data: { id: e.id, source: e.source, target: e.target, relation: e.relation, status: e.status } }));
  if (!cy) initGraph();
  cy.elements().remove();
  cy.add(nodes.concat(edges));
  cy.nodes().forEach((n) => { if (n.data("status") === "superseded") n.addClass("superseded"); });
  cy.edges().forEach((e) => { if (e.data("status") === "superseded") e.addClass("superseded"); });
  buildLegend();
  applyTypeFilter();
  if (g.truncated) {
    $("#graph-sub").textContent = `You + ${g.depth} hops · ${g.nodes.length} of ${g.total_nodes} entities · Reset view for the full graph`;
  } else {
    $("#graph-sub").textContent = `${g.nodes.length} entities · ${g.edges.length} relationships`;
  }
  populateFilterDropdowns(g);
  runGraphLayout();
}

function populateFilterDropdowns(g) {
  const types = (g.entity_types || Object.keys(typeColors)).sort();
  const rels = (g.relation_types || []).sort();
  const fill = (sel, items, label) => {
    const el = $(sel);
    if (!el) return;
    const cur = el.value;
    el.innerHTML = `<option value="">${label}</option>` + items.map((t) => `<option value="${esc(t)}">${esc(t)}</option>`).join("");
    el.value = cur;
  };
  fill("#gf-type", types, "All types");
  fill("#gf-relation", rels, "All relations");
  fill("#sf-type", types, "Any type");
  fill("#browse-type", types, "All types");
}

async function loadBrowse() {
  const list = $("#browse-list");
  if (!list) return;
  const params = new URLSearchParams();
  const q = $("#browse-q") && $("#browse-q").value.trim();
  const type = $("#browse-type") && $("#browse-type").value;
  if (q) params.set("q", q);
  if (type) params.set("type", type);
  if ($("#browse-pinned") && $("#browse-pinned").checked) params.set("pinned", "true");
  if ($("#browse-important") && $("#browse-important").checked) params.set("important", "true");
  const sort = $("#browse-sort") && $("#browse-sort").value;
  if (sort && sort !== "name") params.set("sort", sort);
  const ents = await api("/entities?" + params.toString());
  list.innerHTML = ents.length ? ents.map((e) => `
    <div class="browse-row" data-id="${e.id}">
      <span style="color:${typeColors[e.type] || "#fff"}">●</span>
      <span class="browse-name">${esc(e.name)}</span>
      ${badge(e.type)}
      ${e.pinned ? '<span class="st-status st-pinned">pinned</span>' : ""}
      ${e.important ? '<span class="st-status st-important">important</span>' : ""}
      <span class="browse-meta"><span>${e.degree} links</span><span>${Math.round((e.confidence || 0.8) * 100)}%</span></span>
    </div>`).join("") : `<p class="muted">No entities match.</p>`;
  list.querySelectorAll(".browse-row").forEach((el) =>
    el.addEventListener("click", () => openEntity(el.dataset.id)));
}

async function applyGraphFilters() {
  const params = new URLSearchParams();
  if ($("#gf-type").value) params.set("entity_type", $("#gf-type").value);
  if ($("#gf-relation").value) params.set("relation", $("#gf-relation").value);
  params.set("active_only", $("#gf-superseded").checked ? "false" : "true");
  if ($("#gf-pinned").checked) params.set("pinned", "true");
  if ($("#gf-important").checked) params.set("important", "true");
  const conf = parseFloat($("#gf-confidence") && $("#gf-confidence").value);
  if (conf) params.set("min_confidence", String(conf));
  const g = await api("/graph/filter?" + params.toString());
  cy.elements().remove();
  const nodes = g.nodes.map((n) => ({ data: { id: n.id, label: n.name, type: n.type, description: n.description, pinned: n.pinned, important: n.important, status: n.status } }));
  const edges = g.edges.map((e) => ({ data: { id: e.id, source: e.source, target: e.target, relation: e.relation, status: e.status } }));
  cy.add(nodes.concat(edges));
  cy.nodes().forEach((n) => { if (n.data("status") === "superseded") n.addClass("superseded"); });
  cy.edges().forEach((e) => { if (e.data("status") === "superseded") e.addClass("superseded"); });
  applyConnectedFilter();
  if (g.stats) {
    $("#graph-sub").textContent = `${g.stats.nodes} entities · ${g.stats.edges} relationships · avg degree ${g.stats.avg_degree}`;
  }
  runGraphLayout();
}

const TYPE_RANK = {
  person: 8, project: 7, organization: 6, technology: 5, skill: 4,
  goal: 3, interest: 3, preference: 3, location: 2, topic: 2,
  event: 2, task: 1, fact: 1, concept: 1,
};

function runGraphLayout() {
  if (!cy) return;
  const name = ($("#gf-layout") && $("#gf-layout").value) || "cose";
  if (name === "concentric") {
    cy.layout({
      name: "concentric",
      concentric: (n) => TYPE_RANK[n.data("type")] || 1,
      levelWidth: () => 1,
      animate: true,
      animationDuration: 400,
      padding: 40,
    }).run();
  } else if (name === "breadthfirst") {
    const roots = cy.nodes().filter((n) => String(n.data("label") || "").toLowerCase() === "user");
    cy.layout({
      name: "breadthfirst",
      roots: roots.length ? roots : undefined,
      directed: false,
      spacingFactor: 1.15,
      animate: true,
      animationDuration: 400,
      padding: 40,
    }).run();
  } else {
    cy.layout({
      name: "cose",
      animate: true,
      animationDuration: 500,
      nodeRepulsion: () => 9000,
      idealEdgeLength: () => 90,
      padding: 40,
    }).run();
  }
}

function applyConnectedFilter() {
  if (!cy) return;
  const only = $("#gf-connected") && $("#gf-connected").checked;
  cy.nodes().forEach((n) => {
    const hiddenType = hiddenTypes.has(n.data("type"));
    const isolated = only && n.degree() === 0 && String(n.data("label") || "").toLowerCase() !== "user";
    n.style("display", (hiddenType || isolated) ? "none" : "element");
  });
  cy.edges().forEach((e) => {
    const hidden = e.source().style("display") === "none" || e.target().style("display") === "none";
    e.style("display", hidden ? "none" : "element");
  });
}

$("#graph-apply").addEventListener("click", applyGraphFilters);
if ($("#gf-layout")) $("#gf-layout").addEventListener("change", runGraphLayout);
if ($("#gf-connected")) $("#gf-connected").addEventListener("change", applyConnectedFilter);
if ($("#gf-around-me")) {
  $("#gf-around-me").addEventListener("change", () => {
    buildGraph({ focus: $("#gf-around-me").checked ? "user" : "all" });
  });
}
if ($("#gf-confidence")) {
  $("#gf-confidence").addEventListener("input", (e) => {
    const el = $("#gf-conf-val");
    if (el) el.textContent = e.target.value;
  });
}
if ($("#graph-zoom-in")) $("#graph-zoom-in").addEventListener("click", () => { if (cy) cy.zoom(cy.zoom() * 1.2); });
if ($("#graph-zoom-out")) $("#graph-zoom-out").addEventListener("click", () => { if (cy) cy.zoom(cy.zoom() / 1.2); });
if ($("#graph-fit")) $("#graph-fit").addEventListener("click", () => { if (cy) cy.fit(undefined, 40); });
if ($("#graph-expand")) $("#graph-expand").addEventListener("click", expandSelectedNeighborhood);
if ($("#graph-path")) $("#graph-path").addEventListener("click", showGraphPath);
if ($("#graph-to-me")) $("#graph-to-me").addEventListener("click", pathToUser);

let lastFocusedId = null;
let pathEnds = [];

async function pathToUser() {
  if (!cy) return;
  const id = lastFocusedId || (cy.$("node:selected").length ? cy.$("node:selected")[0].id() : null);
  if (!id) { toast("Select a node first"); return; }
  const roots = cy.nodes().filter((n) => String(n.data("label") || "").toLowerCase() === "user");
  if (!roots.length) { toast("No User node in this view"); return; }
  pathEnds = [String(roots[0].id()), String(id)];
  await showGraphPath();
}

async function showGraphPath() {
  if (pathEnds.length < 2) { toast("Click two nodes, then Path"); return; }
  const [a, b] = pathEnds.slice(-2);
  const g = await api(`/graph/path?source_id=${a}&target_id=${b}`);
  if (!g.found || !g.path) { toast("No stored path between those nodes"); return; }
  cy.elements().addClass("dim").removeClass("highlight");
  const hops = g.path.filter((h) => h.from && h.to);
  hops.forEach((h) => {
    const src = cy.getElementById(String(h.from));
    const tgt = cy.getElementById(String(h.to));
    src.removeClass("dim").addClass("highlight");
    tgt.removeClass("dim").addClass("highlight");
    src.edgesWith(tgt).removeClass("dim").addClass("highlight");
  });
  toast(hops.map((h) => h.relation).join(" → ") || "Path found");
}

async function expandSelectedNeighborhood() {
  if (!cy) return;
  const selected = cy.$("node:selected");
  const id = selected.length ? selected[0].id() : lastFocusedId;
  if (!id) { toast("Select a node first"); return; }
  const g = await api(`/graph/neighborhood/${id}?depth=2`);
  const existing = new Set(cy.nodes().map((n) => String(n.id())));
  const nodes = g.nodes.filter((n) => !existing.has(String(n.id))).map((n) => ({
    data: { id: n.id, label: n.name, type: n.type, pinned: n.pinned, important: n.important, status: n.status },
  }));
  const edges = g.edges.map((e) => ({ data: { id: e.id, source: e.source, target: e.target, relation: e.relation, status: e.status } }));
  if (nodes.length || edges.length) cy.add(nodes.concat(edges));
  const center = cy.getElementById(String(id));
  if (center && center.length) {
    lastFocusedId = id;
    cy.animate({ fit: { eles: center.neighborhood().add(center), padding: 60 }, duration: 300 });
  }
}

$("#graph-search").addEventListener("input", (e) => {
  const q = e.target.value.trim().toLowerCase();
  cy.elements().removeClass("dim");
  if (!q) { cy.fit(undefined, 40); return; }
  cy.nodes().forEach((n) => {
    if (!n.data("label").toLowerCase().includes(q)) n.addClass("dim");
  });
  cy.edges().forEach((ed) => {
    if (ed.source().hasClass("dim") || ed.target().hasClass("dim")) ed.addClass("dim");
  });
  const matches = cy.nodes().filter((n) => !n.hasClass("dim"));
  if (matches.length) cy.animate({ fit: { eles: matches, padding: 60 }, duration: 400 });
});
$("#graph-search").addEventListener("keydown", (e) => { if (e.key === "Escape") { e.target.value = ""; e.target.dispatchEvent(new Event("input")); } });

$("#graph-reset").addEventListener("click", async () => {
  // Reset filter controls and reload the full graph.
  $("#gf-type").value = ""; $("#gf-relation").value = "";
  $("#gf-superseded").checked = false; $("#gf-pinned").checked = false; $("#gf-important").checked = false;
  if ($("#gf-connected")) $("#gf-connected").checked = false;
  if ($("#gf-around-me")) $("#gf-around-me").checked = false;
  if ($("#gf-layout")) $("#gf-layout").value = "cose";
  $$(".legend-row").forEach((r) => r.classList.remove("off"));
  hiddenTypes.clear();
  await buildGraph({ focus: "all" });
  cy.fit(undefined, 50);
  closeEntity();
});

/* ==========================================================================
   Memory timeline (with filters)
   ========================================================================== */
async function loadMemory() {
  const kind = $("#mem-kind").value;
  const entityQ = $("#mem-entity").value.trim();
  const date = $("#mem-date").value;
  const params = new URLSearchParams();
  if (kind) params.set("kind", kind);
  if (date) params.set("date", date);
  if (entityQ) params.set("entity", entityQ);
  const mems = await api("/memories?" + params.toString());
  const byDay = {};
  mems.forEach((m) => {
    const day = fmtDay(m.created_at);
    (byDay[day] = byDay[day] || []).push(m);
  });
  const html = Object.entries(byDay).map(([day, items]) => `
    <div class="tl-day">
      <div class="tl-day-head">${esc(day)}</div>
      ${items.map((m) => {
        return `<div class="tl-item"${m.message_id ? ` data-mid="${m.message_id}" title="Open source message"` : ""}>
          <div class="tl-time">${fmtTime(m.created_at)}</div>
          <div class="tl-text">${esc(m.text)}<span class="tl-kind">${esc(m.kind)}</span>
          ${m.confidence ? `<span class="conf">${Math.round(m.confidence * 100)}%</span>` : ""}</div>
        </div>`;
      }).join("")}
    </div>`).join("");
  $("#timeline").innerHTML = html || `<p class="muted">No memories recorded yet.</p>`;
  $$("#timeline .tl-item").forEach((el) => {
    if (!el.dataset.mid) return;
    el.style.cursor = "pointer";
    el.addEventListener("click", async () => {
      try {
        const src = await api("/messages/" + el.dataset.mid);
        openSource(src);
      } catch (err) { toast(err.message); }
    });
  });
}

$("#mem-kind").addEventListener("change", loadMemory);
$("#mem-date").addEventListener("change", loadMemory);
$("#mem-entity").addEventListener("keydown", (e) => { if (e.key === "Enter") loadMemory(); });
$("#mem-clear").addEventListener("click", () => {
  $("#mem-kind").value = ""; $("#mem-entity").value = ""; $("#mem-date").value = "";
  loadMemory();
});

/* ==========================================================================
   Search
   ========================================================================== */
const REASON_LABELS = {
  keyword: "Keyword match", semantic: "Semantic match",
  graph: "Graph relation", recent: "Recent memory",
  pinned: "Pinned", important: "Important",
};

async function doSearch() {
  const q = $("#search-input").value.trim();
  if (!q) return;
  const body = { query: q };
  if ($("#sf-type").value) body.type = $("#sf-type").value;
  if ($("#sf-confidence").value) body.min_confidence = parseFloat($("#sf-confidence").value);
  if ($("#sf-status").value) body.status = $("#sf-status").value;
  if ($("#sf-pinned").checked) body.pinned = true;
  if ($("#sf-important").checked) body.important = true;
  if ($("#sf-from") && $("#sf-from").value) body.date_from = $("#sf-from").value;
  if ($("#sf-to") && $("#sf-to").value) body.date_to = $("#sf-to").value;
  if ($("#sf-source") && $("#sf-source").value) body.source = $("#sf-source").value;

  const r = await api("/search", { method: "POST", body: JSON.stringify(body) });
  const ans = $("#search-answer");
  ans.style.display = "block";
  const stLabel = { answered: "known", known: "known", unknown: "unknown", uncertain: "uncertain" }[r.status] || r.status;
  ans.innerHTML = `<div class="panel-head"><h2>Answer <span class="ans-status ans-${r.status}">${stLabel}</span></h2></div>
    <div class="panel-body">${esc(r.answer)}</div>`;

  // Sources used (traceable).
  const srcPanel = $("#search-sources");
  if (r.sources && r.sources.length) {
    srcPanel.style.display = "block";
    srcPanel.innerHTML = `<div class="panel-head"><h2>Sources used</h2></div><div class="panel-body">
      ${r.sources.map((s) => `
        <span class="remembered-chip" data-id="${s.entity_id}">
          <span style="color:${typeColors[s.type] || "#fff"}">●</span> ${esc(s.name)}
          ${s.conversation_title ? ` · <span class="conf">${esc(s.conversation_title)}</span>` : ""}
          ${s.snippet ? ` · <span class="conf">${esc(s.snippet)}</span>` : ""}
        </span>`).join("")}
    </div>`;
    srcPanel.querySelectorAll(".remembered-chip").forEach((chip) =>
      chip.addEventListener("click", () => openEntity(chip.dataset.id)));
  } else {
    srcPanel.style.display = "none";
  }

  $("#search-results").innerHTML = r.entities.length ? `
    <div class="panel"><div class="panel-head"><h2>Entities</h2></div><div class="panel-body">
      ${r.entities.map((e) => `
        <div class="result-entity" data-id="${e.id}">
          <span style="color:${typeColors[e.type] || "#fff"}">●</span>
          <div style="flex:1">
            <div class="re-name">${esc(e.name)} <span class="conf">${Math.round((e.confidence || 0.8) * 100)}%</span></div>
            <div class="re-desc">${esc(e.description || "")}</div>
            <div class="re-reasons">${(e.reasons || []).map((r) => `<span class="reason-chip">${esc(REASON_LABELS[r] || r)}</span>`).join("")}</div>
          </div>
          ${badge(e.type)}
        </div>`).join("")}
    </div></div>
    <div class="panel"><div class="panel-head"><h2>Facts</h2></div><div class="panel-body">
      ${r.facts.map((f) => `<div class="mem-item"><span class="mem-ico">⇄</span><span class="mem-text">${esc(f.text)}</span></div>`).join("")}
    </div></div>`
    : `<p class="muted">Nothing found for “${esc(q)}”.</p>`;
  $$("#search-results .result-entity").forEach((el) =>
    el.addEventListener("click", () => openEntity(el.dataset.id)));
}
$("#search-btn").addEventListener("click", doSearch);
$("#search-input").addEventListener("keydown", (e) => { if (e.key === "Enter") doSearch(); });

/* ==========================================================================
   Entity slide-over
   ========================================================================== */
let currentEntity = null;

function openEntity(id) {
  loadEntity(id);
  $("#entity-panel").classList.add("open");
  $("#entity-overlay").classList.add("show");
  if (id != null && id !== "") setHash("entity", id);
}
function closeEntity() {
  $("#entity-panel").classList.remove("open");
  $("#entity-overlay").classList.remove("show");
  currentEntity = null;
  if (parseHash().view === "entity") setHash(currentView || "dashboard");
}
$("#entity-overlay").addEventListener("click", closeEntity);

function openSource(source) {
  if (!source) return;
  const modal = document.createElement("div");
  modal.className = "modal src-modal";
  modal.innerHTML = `
    <div class="modal-card">
      <h3>Source</h3>
      <p class="muted">${source.conversation_title ? "Conversation: " + esc(source.conversation_title) : "Conversation"} · ${fmtDay(source.created_at)}</p>
      <div class="msg-bubble">${esc(source.content)}</div>
      <div style="margin-top:12px;text-align:right"><button class="btn-ghost" id="src-close">Close</button></div>
    </div>`;
  document.body.appendChild(modal);
  modal.addEventListener("click", (e) => { if (e.target === modal) modal.remove(); });
  modal.querySelector("#src-close").addEventListener("click", () => modal.remove());
}

async function loadEntity(id) {
  currentEntity = id;
  const d = await api("/entities/" + id);
  const e = d.entity;

  const relTypes = ["learning","uses","knows","likes","created","interested_in","related_to","wants","works_on","prefers","works_at","lives_in","located_in","member_of"];
  const related = d.related.map((r) => `
    <div class="rel-item ${r.status === "superseded" ? "super" : ""}" data-id="${r.other_id}">
      <span style="color:${typeColors[r.other_type] || "#fff"}">●</span>
      <span class="ri-name">${esc(r.other_name)}</span>
      ${badge(r.other_type)}
      <span class="rel-conf">${Math.round((r.confidence || 0.8) * 100)}%</span>
      <span class="ri-rel">${r.direction === "out" ? "→" : "←"} ${esc(r.relation)}</span>
      ${r.rid ? `<select class="input rel-edit" data-rid="${r.rid}" title="Change relationship type">${relTypes.map((t) => `<option value="${t}" ${(r.canonical || r.relation) === t ? "selected" : ""}>${t}</option>`).join("")}</select>` : ""}
      ${r.rid ? `<button class="rel-del" data-rid="${r.rid}" title="Delete relationship">✕</button>` : ""}
    </div>`).join("");

  const flags = [];
  if (e.pinned) flags.push('<span class="st-status st-pinned">pinned</span>');
  if (e.important) flags.push('<span class="st-status st-important">important</span>');
  if (e.status === "superseded") flags.push('<span class="st-status st-superseded">superseded</span>');
  if (e.meta && e.meta.demo) flags.push('<span class="st-status st-demo">demo</span>');

  const aliases = (e.aliases || []).length ? (e.aliases || []).map(esc).join(", ") : "—";

  $("#entity-inner").innerHTML = `
    <button class="entity-close" id="entity-close">✕</button>
    <div class="entity-title">${esc(e.name)}</div>
    <div style="margin:6px 0 2px">${badge(e.type)}</div>
    <div class="entity-meta">${flags.join(" ")}</div>
    <div class="entity-desc">${esc(e.description || "No description.")}</div>

    <div class="conf-label">Confidence: ${Math.round((e.confidence || 0.8) * 100)}%</div>
    <div class="conf-bar"><div class="conf-fill" style="width:${Math.round((e.confidence || 0.8) * 100)}%"></div></div>

    <div class="entity-sec">
      <h3>Details</h3>
      <div class="meta-kv">Aliases: <b>${aliases}</b></div>
      <div class="meta-kv">Embedding: <b>${e.embedding ? "stored" : "none"}</b></div>
      <div class="meta-kv">Created: <b>${fmtDay(e.created_at)} ${fmtTime(e.created_at)}</b></div>
      <div class="meta-kv">Updated: <b>${fmtDay(e.updated_at)} ${fmtTime(e.updated_at)}</b></div>
      ${e.source ? `<div class="meta-kv">Source: <span class="source-link" id="entity-source">${e.source.conversation_title ? esc(e.source.conversation_title) : "conversation"} · ${fmtDay(e.source.created_at)}</span></div>` : ""}
    </div>

    <div class="entity-sec">
      <h3>Relationships (${d.related.length})</h3>
      ${related || `<p class="muted">None yet.</p>`}
      <div class="form" style="margin-top:10px">
        <label class="field"><span>Add relationship</span>
          <select class="input" id="add-rel-type">
            <option value="related_to">related_to</option>
            <option value="uses">uses</option>
            <option value="learning">learning</option>
            <option value="works_on">works_on</option>
            <option value="knows">knows</option>
            <option value="likes">likes</option>
            <option value="created">created</option>
            <option value="interested_in">interested_in</option>
            <option value="wants">wants</option>
            <option value="prefers">prefers</option>
            <option value="works_at">works_at</option>
            <option value="lives_in">lives_in</option>
            <option value="member_of">member_of</option>
          </select>
        </label>
        <input class="input" id="add-rel-target" placeholder="Target entity name" />
        <button class="btn-ghost" id="add-rel-btn">Add</button>
      </div>
    </div>

    <div class="entity-sec">
      <h3>Current state</h3>
      ${(d.history && d.history.current.length) ? d.history.current.map((r) => `
        <div class="entity-mem">${esc(r.text)} <span class="muted" style="font-size:11px">${Math.round((r.confidence || 0.8) * 100)}%</span></div>`).join("")
        : `<p class="muted">No active relationships.</p>`}
    </div>

    ${(d.history && d.history.superseded.length) ? `
    <div class="entity-sec">
      <h3>Previous (superseded)</h3>
      ${d.history.superseded.map((r) => `
        <div class="entity-mem super">${esc(r.text)} <span class="muted" style="font-size:11px">${fmtTime(r.created_at)}</span></div>`).join("")}
    </div>` : ""}

    ${(d.history && d.history.changes.length) ? `
    <div class="entity-sec">
      <h3>Changes</h3>
      ${d.history.changes.map((c) => `
        <div class="entity-mem">${esc(c.text)} <span class="muted" style="font-size:11px">${fmtTime(c.created_at)} · ${esc(c.kind)}</span></div>`).join("")}
    </div>` : ""}

    ${(d.similar && d.similar.length) ? `
    <div class="entity-sec">
      <h3>Looks similar</h3>
      ${d.similar.map((s) => `
        <div class="rel-item" data-id="${s.id}">
          <span style="color:${typeColors[s.type] || "#fff"}">●</span>
          <span class="ri-name">${esc(s.name)}</span>
          ${badge(s.type)}
          <span class="rel-conf">${Math.round((s.score || 0) * 100)}%</span>
        </div>`).join("")}
      <p class="muted">Possible duplicates. Use Merge if they are the same thing.</p>
    </div>` : ""}

    <div class="entity-sec">
      <h3>Memory history</h3>
      ${d.memories.length ? d.memories.map((m) => `
        <div class="entity-mem">${esc(m.text)}<br><span class="muted" style="font-size:11px">${fmtTime(m.created_at)} · ${esc(m.kind)}</span></div>`).join("")
        : `<p class="muted">None.</p>`}
    </div>

    <div class="entity-sec" id="entity-edit-sec" style="display:none">
      <h3>Edit</h3>
      <div class="form">
        <label class="field"><span>Name</span><input class="input" id="edit-name" value="${esc(e.name)}"></label>
        <label class="field"><span>Type</span>
          <select class="input" id="edit-type">
            ${Object.keys(typeColors).map((t) => `<option value="${t}" ${t === e.type ? "selected" : ""}>${t}</option>`).join("")}
          </select>
        </label>
        <label class="field"><span>Description</span><textarea class="input" id="edit-desc" rows="3">${esc(e.description || "")}</textarea></label>
        <label class="field"><span>Confidence</span><input class="input" id="edit-conf" type="number" min="0" max="1" step="0.05" value="${e.confidence}"></label>
        <div style="display:flex;gap:8px">
          <button class="btn-primary" id="edit-save">Save</button>
          <button class="btn-ghost" id="edit-cancel">Cancel</button>
        </div>
      </div>
    </div>

    <div class="entity-actions">
      <button class="btn-ghost" id="act-edit">Edit</button>
      <button class="btn-ghost" id="act-pin">${e.pinned ? "Unpin" : "Pin"}</button>
      <button class="btn-ghost" id="act-important">${e.important ? "Unmark important" : "Mark important"}</button>
      <button class="btn-ghost" id="act-focus">Focus in graph</button>
      <button class="btn-ghost" id="act-merge">Merge…</button>
      <button class="btn-danger" id="act-delete">Delete</button>
    </div>`;

  $("#entity-close").addEventListener("click", closeEntity);
  const srcLink = $("#entity-source");
  if (srcLink) srcLink.addEventListener("click", () => openSource(e.source));
  $$("#entity-inner .rel-item").forEach((el) =>
    el.addEventListener("click", (ev) => {
      if (ev.target.closest(".rel-del") || ev.target.closest(".rel-edit")) return;
      openEntity(el.dataset.id);
    }));
  $$("#entity-inner .rel-edit").forEach((sel) =>
    sel.addEventListener("change", async (ev) => {
      ev.stopPropagation();
      await api("/relationships/" + sel.dataset.rid, {
        method: "PATCH", body: JSON.stringify({ relation: sel.value }),
      });
      toast("Relationship updated");
      loadEntity(id); buildGraph();
    }));
  $$("#entity-inner .rel-del").forEach((btn) =>
    btn.addEventListener("click", async (ev) => {
      ev.stopPropagation();
      if (!confirm("Delete this relationship?")) return;
      await api("/relationships/" + btn.dataset.rid, { method: "DELETE" });
      toast("Relationship deleted");
      loadEntity(id); buildGraph();
    }));
  $("#act-edit").addEventListener("click", () => $("#entity-edit-sec").style.display = "block");
  $("#edit-cancel").addEventListener("click", () => $("#entity-edit-sec").style.display = "none");
  $("#edit-save").addEventListener("click", async () => {
    await api("/entities/" + id, { method: "PATCH", body: JSON.stringify({
      name: $("#edit-name").value, type: $("#edit-type").value,
      description: $("#edit-desc").value, confidence: parseFloat($("#edit-conf").value),
    })});
    toast("Entity updated");
    loadEntity(id); buildGraph(); loadDashboard();
  });
  $("#act-pin").addEventListener("click", async () => {
    await api("/entities/" + id, { method: "PATCH", body: JSON.stringify({ pinned: !e.pinned }) });
    toast(e.pinned ? "Unpinned" : "Pinned");
    loadEntity(id); buildGraph(); loadDashboard();
  });
  $("#act-important").addEventListener("click", async () => {
    await api("/entities/" + id, { method: "PATCH", body: JSON.stringify({ important: !e.important }) });
    toast(e.important ? "Unmarked" : "Marked important");
    loadEntity(id); buildGraph(); loadDashboard();
  });
  $("#act-focus").addEventListener("click", () => {
    showView("graph");
    lastFocusedId = id;
    cy.elements().addClass("dim");
    const n = cy.getElementById(String(id));
    n.removeClass("dim");
    n.neighborhood().removeClass("dim");
    if (n && n.length) n.select();
    cy.animate({ fit: { eles: n.neighborhood().add(n), padding: 80 }, duration: 400 });
    closeEntity();
  });
  const addRelBtn = $("#add-rel-btn");
  if (addRelBtn) addRelBtn.addEventListener("click", async () => {
    const name = ($("#add-rel-target").value || "").trim();
    const rel = $("#add-rel-type").value;
    if (!name) return;
    const ents = await api("/entities?q=" + encodeURIComponent(name));
    const hit = ents.find((x) => x.name.toLowerCase() === name.toLowerCase()) || ents[0];
    if (!hit) { toast("No matching entity"); return; }
    await api("/relationships", { method: "POST", body: JSON.stringify({
      source_id: Number(id), target_id: hit.id, relation: rel,
    })});
    toast("Relationship added");
    loadEntity(id); buildGraph(); loadDashboard();
  });
  $("#act-merge").addEventListener("click", () => openMerge(id));
  $("#act-delete").addEventListener("click", async () => {
    if (!confirm("Delete this entity and its relationships?")) return;
    try {
      await api("/entities/" + id, { method: "DELETE" });
      toast("Entity deleted");
      closeEntity(); buildGraph(); loadDashboard();
    } catch (err) { toast(err.message); }
  });
}

function openMerge(dropId) {
  const modal = document.createElement("div");
  modal.className = "modal";
  modal.innerHTML = `
    <div class="modal-card">
      <h3>Merge into another entity</h3>
      <p class="muted">This entity's relationships will be re-wired to the chosen target.</p>
      <input class="input modal-search" placeholder="Search entities…" />
      <div class="modal-list"></div>
      <div style="margin-top:12px;text-align:right"><button class="btn-ghost" id="merge-cancel">Cancel</button></div>
    </div>`;
  document.body.appendChild(modal);
  modal.addEventListener("click", (e) => { if (e.target === modal) modal.remove(); });
  modal.querySelector("#merge-cancel").addEventListener("click", () => modal.remove());

  const input = modal.querySelector(".modal-search");
  const list = modal.querySelector(".modal-list");
  async function render(q = "") {
    const ents = await api("/entities");
    const filtered = ents.filter((e) => e.id !== dropId && e.name.toLowerCase().includes(q.toLowerCase())).slice(0, 40);
    list.innerHTML = filtered.map((e) => `
      <div class="modal-opt" data-id="${e.id}">
        <span style="color:${typeColors[e.type] || "#fff"}">●</span>
        <span>${esc(e.name)}</span>${badge(e.type)}
      </div>`).join("");
    list.querySelectorAll(".modal-opt").forEach((el) =>
      el.addEventListener("click", async () => {
        await api("/entities/merge", { method: "POST", body: JSON.stringify({ keep_id: el.dataset.id, drop_id: dropId }) });
        toast("Merged");
        modal.remove();
        closeEntity(); buildGraph(); loadDashboard();
      }));
  }
  input.addEventListener("input", () => render(input.value));
  render();
}

/* ==========================================================================
   Settings
   ========================================================================== */
async function loadSettings() {
  const s = await api("/settings");
  $("#set-llm").value = s.llm_model;
  $("#set-emb").value = s.embedding_model;
  $("#set-ollama-url").value = s.ollama_base_url;
  $("#set-confidence").value = s.confidence_threshold;
  $("#conf-val").textContent = s.confidence_threshold;
  $("#set-merge").value = s.merge_similarity;
  $("#merge-val").textContent = s.merge_similarity;
  $("#set-auto-memory").checked = s.auto_memory;
  if ($("#set-auto-backup")) {
    const hours = (s.auto_backup_hours == null ? 24 : s.auto_backup_hours);
    $("#set-auto-backup").value = String([0, 6, 12, 24, 48].includes(Number(hours)) ? hours : 24);
  }
  if ($("#set-theme")) $("#set-theme").value = s.theme || "dark";
  $("#db-path").textContent = "Database: " + s.db_path;
  $("#ollama-info").innerHTML = s.ollama_available
    ? `<p class="hint">Ollama is <span style="color:var(--ok)">online</span>.</p>
       <p class="hint">Installed models: ${s.models_installed.map(esc).join(", ") || "none"}</p>`
    : `<p class="hint">Ollama is <span style="color:var(--danger)">offline</span> — running the built-in rule-based extractor.</p>
       <p class="hint">Start it with <code>ollama serve</code> and pull <code>qwen3:0.6b</code> + <code>nomic-embed-text</code>.</p>`;
  const priv = s.privacy || {};
  const pbox = $("#privacy-info");
  if (pbox) {
    pbox.innerHTML = `
      <p class="hint">Architecture: <strong>${esc((priv.mode || "local-first").toUpperCase())}</strong></p>
      <p class="hint">Local: ${priv.local === false ? "no" : "yes"} · Private: ${priv.private === false ? "no" : "yes"} · Telemetry: ${priv.telemetry ? "on" : "off"} · Cloud: ${priv.cloud ? "yes" : "none"}</p>
      <p class="hint">Personal memory stays on this machine unless you export it yourself.</p>
      <p class="hint">Database: <code>${esc(s.db_path || "")}</code> · Integrity: <strong>${s.db_ok === false ? "not ok" : "ok"}</strong></p>
      <p class="hint">Activity watch: ${priv.activity_watch ? "on" : "off"} — Second Brain never screenshots or polls what you are doing.</p>`;
  }
  document.body.classList.toggle("theme-light", s.theme === "light");
}

$("#set-confidence").addEventListener("input", (e) => { $("#conf-val").textContent = e.target.value; });
$("#set-merge").addEventListener("input", (e) => { $("#merge-val").textContent = e.target.value; });

$("#set-save").addEventListener("click", async () => {
  await api("/settings", { method: "POST", body: JSON.stringify({
    llm_model: $("#set-llm").value.trim() || undefined,
    embedding_model: $("#set-emb").value.trim() || undefined,
    ollama_base_url: $("#set-ollama-url").value.trim() || undefined,
  })});
  $("#set-hint").textContent = "Saved. Models are now active.";
  refreshStatus();
});

$("#set-behavior-save").addEventListener("click", async () => {
  await api("/settings", { method: "POST", body: JSON.stringify({
    confidence_threshold: parseFloat($("#set-confidence").value),
    merge_similarity: parseFloat($("#set-merge").value),
    auto_memory: $("#set-auto-memory").checked,
    auto_backup_hours: $("#set-auto-backup") ? parseFloat($("#set-auto-backup").value) : undefined,
    theme: $("#set-theme") ? $("#set-theme").value : undefined,
  })});
  if ($("#set-theme")) document.body.classList.toggle("theme-light", $("#set-theme").value === "light");
  toast("Memory behavior saved");
});

$("#reset-btn").addEventListener("click", async () => {
  if (!confirm("Wipe ALL entities, relationships, memories and messages?")) return;
  await api("/reset", { method: "POST", body: JSON.stringify({ confirm: true }) });
  toast("All data cleared");
  location.reload();
});

$("#demo-btn").addEventListener("click", async () => {
  await api("/demo", { method: "POST" });
  toast("Demo data loaded (marked as DEMO)");
  loadDashboard(); buildGraph(); loadMemory(); loadConversations();
});

if ($("#demo-clear-btn")) {
  $("#demo-clear-btn").addEventListener("click", async () => {
    if (!confirm("Remove demo-marked entities and the demo conversation? Real memories stay.")) return;
    const r = await api("/demo/clear", { method: "POST" });
    toast(`Removed ${r.entities_removed || 0} demo entities`);
    loadDashboard(); buildGraph(); loadMemory(); loadConversations();
  });
}

/* ---- Export / Import / Backup / Summarize ---- */

function downloadBlob(content, filename, type) {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url; a.download = filename;
  document.body.appendChild(a); a.click(); a.remove();
  URL.revokeObjectURL(url);
}

$("#export-json").addEventListener("click", async () => {
  const r = await fetch(API + "/export/json");
  downloadBlob(await r.text(), "second-brain-export.json", "application/json");
  toast("JSON exported");
});

$("#export-md").addEventListener("click", async () => {
  const r = await fetch(API + "/export/markdown");
  downloadBlob(await r.text(), "second-brain-export.md", "text/markdown");
  toast("Markdown exported");
});

function formatImportReport(r) {
  if (!r || !r.ok) return "Error: " + ((r && r.error) || "import failed");
  let msg = r.mode === "replace"
    ? `Replaced: ${r.entities_created} entities imported.`
    : `Merged: ${r.entities_created} created, ${r.entities_merged} merged, ${r.relationships_added} relationships.`;
  const conflicts = r.conflicts || (r.report && r.report.conflicts) || [];
  if (conflicts.length) {
    msg += " Conflicts: " + conflicts.slice(0, 8).map((c) =>
      `${c.relation} now ${c.kept} (was ${c.superseded})`).join("; ") + ".";
  }
  const skippedRels = r.relationships_skipped || 0;
  const skippedMems = r.memories_skipped || 0;
  if (skippedRels) msg += ` Skipped ${skippedRels} relationship(s).`;
  if (skippedMems) msg += ` ${skippedMems} duplicate memories ignored.`;
  return msg;
}

$("#import-merge").addEventListener("click", async () => {
  const data = $("#import-data").value.trim();
  if (!data) return;
  try {
    const r = await api("/import", { method: "POST", body: JSON.stringify({ data, mode: "merge" }) });
    $("#import-status").textContent = formatImportReport(r);
    if (r.ok) { loadDashboard(); buildGraph(); }
  } catch (e) { $("#import-status").textContent = "Error: " + e.message; }
});

$("#import-replace").addEventListener("click", async () => {
  const data = $("#import-data").value.trim();
  if (!data) return;
  if (!confirm("Replace the ENTIRE database with this import? This wipes all current data.")) return;
  try {
    const r = await api("/import", { method: "POST", body: JSON.stringify({ data, mode: "replace", confirm: true }) });
    $("#import-status").textContent = formatImportReport(r);
    if (r.ok) { loadDashboard(); buildGraph(); loadMemory(); }
  } catch (e) { $("#import-status").textContent = "Error: " + e.message; }
});

if ($("#import-notes-btn")) {
  $("#import-notes-btn").addEventListener("click", async () => {
    const text = ($("#import-notes") && $("#import-notes").value || "").trim();
    if (!text) return;
    try {
      const r = await api("/import/notes", { method: "POST", body: JSON.stringify({ text }) });
      $("#import-status").textContent = r.ok
        ? `Imported ${r.chunks} note(s), ${r.remembered} memories.`
        : "Error: " + (r.error || "failed");
      if (r.ok) { loadDashboard(); buildGraph(); loadMemory(); loadConversations(); }
    } catch (e) { $("#import-status").textContent = "Error: " + e.message; }
  });
}

$("#backup-now").addEventListener("click", async () => {
  const r = await api("/backup", { method: "POST" });
  $("#backup-status").textContent = r.ok
    ? `Backup created at ${r.path} (db: ${r.db}, json: ${r.export_json}, md: ${r.export_md})`
    : "Backup failed";
  loadBackupStatus();
});

async function loadBackupStatus() {
  try {
    const s = await api("/backup/status");
    if (s.count) {
      $("#backup-status").textContent = `Last backup: ${s.last_backup_at || "—"} · ${s.count} total · ${s.backup_dir}`;
    }
    const box = $("#backup-list");
    if (!box) return;
    const items = s.backups || [];
    box.innerHTML = items.length ? items.slice(0, 8).map((b) => `
      <div class="browse-row" style="margin-top:8px">
        <span class="browse-name">${esc(b.name)}</span>
        <span class="browse-meta">${esc((b.created_at || "").slice(0, 19))}${b.bytes ? " · " + Math.round(b.bytes / 1024) + " KB" : ""}${b.has_db === false ? " · missing db" : ""}</span>
        <button class="btn-ghost backup-restore" data-name="${esc(b.name)}">Restore</button>
      </div>`).join("") : "";
    box.querySelectorAll(".backup-restore").forEach((btn) =>
      btn.addEventListener("click", async () => {
        if (!confirm("Restore this backup? A safety snapshot of the current brain is created first.")) return;
        try {
          const r = await api("/backup/restore", {
            method: "POST",
            body: JSON.stringify({ name: btn.dataset.name, confirm: true }),
          });
          toast(r.ok ? "Backup restored" : "Restore failed");
          if (r.ok) { loadDashboard(); buildGraph(); loadMemory(); loadConversations(); loadBrowse(); }
        } catch (e) { toast(e.message); }
      }));
  } catch {}
}

async function loadSummarizeCandidates() {
  try {
    const cands = await api("/summarize/candidates");
    $("#summarize-candidates").innerHTML = cands.length
      ? `<p class="hint">Ready to summarize:</p>` + cands.slice(0, 5).map((c) =>
          `<div class="mem-item"><span class="mem-ico">Σ</span><span class="mem-text">${esc(c.entity_name)} <span class="muted">(${c.count} memories)</span></span></div>`).join("")
      : `<p class="hint">No clusters ready for summarization yet.</p>`;
  } catch {}
}

$("#summarize-all").addEventListener("click", async () => {
  $("#summarize-status").textContent = "Summarizing…";
  try {
    const r = await api("/summarize", { method: "POST", body: JSON.stringify({}) });
    const okCount = Array.isArray(r) ? r.filter((x) => x && x.ok).length : (r.ok ? 1 : 0);
    $("#summarize-status").textContent = `Summarized ${okCount} entit${okCount === 1 ? "y" : "ies"}.`;
    loadSummarizeCandidates(); loadDashboard();
  } catch (e) { $("#summarize-status").textContent = "Error: " + e.message; }
});

/* ==========================================================================
   Command palette + keyboard
   ========================================================================== */
let paletteIndex = 0;
let paletteItems = [];

function closePalette() {
  const pal = $("#palette");
  const ov = $("#palette-overlay");
  if (pal) pal.hidden = true;
  if (ov) ov.classList.remove("show");
}

function openPalette() {
  const pal = $("#palette");
  const ov = $("#palette-overlay");
  const input = $("#palette-input");
  if (!pal || !input) return;
  pal.hidden = false;
  if (ov) ov.classList.add("show");
  input.value = "";
  input.focus();
  renderPalette("");
}

async function renderPalette(q) {
  const box = $("#palette-results");
  if (!box) return;
  const query = (q || "").trim().toLowerCase();
  const views = VIEWS.map((v) => ({ kind: "view", id: v, label: v[0].toUpperCase() + v.slice(1) }));
  let ents = [];
  let convs = [];
  try { ents = await api("/entities" + (query ? ("?q=" + encodeURIComponent(query)) : "")); } catch {}
  try { convs = await api("/conversations" + (query ? ("?q=" + encodeURIComponent(query)) : "")); } catch {}
  const viewHits = views.filter((v) => !query || v.label.toLowerCase().includes(query));
  const entHits = ents.slice(0, 10).map((e) => ({ kind: "entity", id: e.id, label: e.name, type: e.type }));
  const convHits = (convs || []).slice(0, 6).map((c) => ({ kind: "conversation", id: c.id, label: c.title || ("Chat " + c.id) }));
  paletteItems = viewHits.concat(convHits, entHits);
  paletteIndex = 0;
  box.innerHTML = paletteItems.map((it, i) => `
    <div class="palette-item ${i === 0 ? "active" : ""}" data-i="${i}">
      <span class="palette-kicker">${it.kind}</span>
      <span>${esc(it.label)}</span>
      ${it.type ? badge(it.type) : ""}
    </div>`).join("") || `<p class="muted">Nothing matches.</p>`;
  box.querySelectorAll(".palette-item").forEach((el) =>
    el.addEventListener("click", () => choosePalette(Number(el.dataset.i))));
}

function choosePalette(i) {
  const it = paletteItems[i];
  closePalette();
  if (!it) return;
  if (it.kind === "view") showView(it.id);
  else if (it.kind === "conversation") { showView("chat"); openConversation(it.id); }
  else openEntity(it.id);
}

if ($("#palette-input")) {
  $("#palette-input").addEventListener("input", (e) => renderPalette(e.target.value));
  $("#palette-input").addEventListener("keydown", (e) => {
    if (e.key === "ArrowDown") { e.preventDefault(); paletteIndex = Math.min(paletteItems.length - 1, paletteIndex + 1); }
    if (e.key === "ArrowUp") { e.preventDefault(); paletteIndex = Math.max(0, paletteIndex - 1); }
    $$("#palette-results .palette-item").forEach((el, i) => el.classList.toggle("active", i === paletteIndex));
    if (e.key === "Enter") { e.preventDefault(); choosePalette(paletteIndex); }
    if (e.key === "Escape") closePalette();
  });
}
if ($("#palette-overlay")) $("#palette-overlay").addEventListener("click", closePalette);
if ($("#browse-q")) $("#browse-q").addEventListener("input", loadBrowse);
if ($("#browse-type")) $("#browse-type").addEventListener("change", loadBrowse);
if ($("#browse-pinned")) $("#browse-pinned").addEventListener("change", loadBrowse);
if ($("#browse-important")) $("#browse-important").addEventListener("change", loadBrowse);
if ($("#browse-sort")) $("#browse-sort").addEventListener("change", loadBrowse);

document.addEventListener("keydown", (e) => {
  const tag = (e.target && e.target.tagName) || "";
  const typing = tag === "INPUT" || tag === "TEXTAREA" || (e.target && e.target.isContentEditable);
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
    e.preventDefault();
    const pal = $("#palette");
    if (pal && !pal.hidden) closePalette();
    else openPalette();
    return;
  }
  if (e.key === "Escape") {
    closePalette();
    closeEntity();
    return;
  }
  if (typing) return;
  const map = { "1": "dashboard", "2": "chat", "3": "graph", "4": "browse", "5": "memory", "6": "search", "7": "settings" };
  if (map[e.key]) showView(map[e.key]);
  if (e.key === "/") { e.preventDefault(); showView("search"); const el = $("#search-input"); if (el) el.focus(); }
});

/* ==========================================================================
   Boot
   ========================================================================== */
async function boot() {
  const wanted = location.hash;
  refreshStatus();
  await loadChatHistory();
  await buildGraph();
  await loadDashboard();
  await loadSettings();
  loadBackupStatus();
  loadSummarizeCandidates();
  loadConversations();
  if (wanted && wanted !== "#") {
    try { history.replaceState(null, "", wanted); } catch {}
    applyRoute();
  } else {
    showView("dashboard");
  }
  setInterval(refreshStatus, 15000);
}
boot();
