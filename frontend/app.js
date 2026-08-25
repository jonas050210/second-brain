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
const VIEWS = ["dashboard", "chat", "graph", "memory", "search", "settings"];

function showView(name) {
  VIEWS.forEach((v) => $("#view-" + v).classList.toggle("active", v === name));
  $$(".nav-item").forEach((b) => b.classList.toggle("active", b.dataset.view === name));
  if (name === "graph") requestAnimationFrame(() => { if (cy) cy.fit(undefined, 30); });
  if (name === "dashboard") loadDashboard();
  if (name === "memory") loadMemory();
  if (name === "chat") scrollChat();
}

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

  if (d.has_demo_data) {
    toast("This database contains demo data — it's marked with a DEMO badge.");
  }
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

  const t = document.createElement("div");
  t.className = "msg-time";
  t.textContent = fmtTime(new Date().toISOString());
  wrap.appendChild(t);
  $("#chat-messages").appendChild(wrap);
  scrollChat();
}

async function sendChat() {
  const input = $("#chat-input");
  const content = input.value.trim();
  if (!content) return;
  input.value = "";
  input.style.height = "auto";
  appendMessage("user", content);
  $("#chat-send").disabled = true;
  try {
    const r = await api("/chat", {
      method: "POST",
      body: JSON.stringify({ content, conversation_id: currentConversationId }),
    });
    if (r.conversation_id) currentConversationId = r.conversation_id;
    appendMessage("assistant", r.reply, {
      remembered: r.remembered,
      superseded: r.superseded,
      status: r.status,
    });
    if (r.remembered && r.remembered.length) { loadDashboard(); buildGraph(); }
    if (r.is_command || r.remembered) loadDashboard();
  } catch (e) {
    appendMessage("assistant", "⚠ " + e.message);
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
  $("#chat-messages").innerHTML = "";
  $("#chat-empty").style.display = "";
  toast("Started a new conversation");
});

async function loadChatHistory() {
  const convs = await api("/conversations");
  if (!convs.length) return;
  const latest = convs[0];
  currentConversationId = latest.id;
  const msgs = await api(`/conversations/${latest.id}/messages`);
  msgs.forEach((m) => {
    if (m.role === "user") appendMessage("user", m.content);
    else appendMessage("assistant", m.content, { remembered: m.remembered, kind: m.kind });
  });
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

  cy.on("tap", "node", (e) => openEntity(e.target.id()));
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
  cy.nodes().forEach((n) => {
    n.style("display", hiddenTypes.has(n.data("type")) ? "none" : "element");
  });
  cy.edges().forEach((e) => {
    const hidden = hiddenTypes.has(e.source().data("type")) || hiddenTypes.has(e.target().data("type"));
    e.style("display", hidden ? "none" : "element");
  });
}

async function buildGraph() {
  const g = await api("/graph");
  graphNodes = g.nodes;
  typeColors = g.type_colors || TYPE_COLORS;
  const nodes = g.nodes.map((n) => ({ data: { id: n.id, label: n.label, type: n.type, description: n.description, pinned: n.pinned, important: n.important, status: n.status } }));
  const edges = g.edges.map((e) => ({ data: { id: e.id, source: e.source, target: e.target, relation: e.relation, status: e.status } }));
  if (!cy) initGraph();
  cy.elements().remove();
  cy.add(nodes.concat(edges));
  cy.nodes().forEach((n) => { if (n.data("status") === "superseded") n.addClass("superseded"); });
  cy.edges().forEach((e) => { if (e.data("status") === "superseded") e.addClass("superseded"); });
  buildLegend();
  applyTypeFilter();
  $("#graph-sub").textContent = `${g.nodes.length} entities · ${g.edges.length} relationships`;
  populateFilterDropdowns(g);
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
}

async function applyGraphFilters() {
  const params = new URLSearchParams();
  if ($("#gf-type").value) params.set("entity_type", $("#gf-type").value);
  if ($("#gf-relation").value) params.set("relation", $("#gf-relation").value);
  params.set("active_only", $("#gf-superseded").checked ? "false" : "true");
  if ($("#gf-pinned").checked) params.set("pinned", "true");
  if ($("#gf-important").checked) params.set("important", "true");
  const g = await api("/graph/filter?" + params.toString());
  cy.elements().remove();
  const nodes = g.nodes.map((n) => ({ data: { id: n.id, label: n.name, type: n.type, description: n.description, pinned: n.pinned, important: n.important, status: n.status } }));
  const edges = g.edges.map((e) => ({ data: { id: e.id, source: e.source, target: e.target, relation: e.relation, status: e.status } }));
  cy.add(nodes.concat(edges));
  cy.nodes().forEach((n) => { if (n.data("status") === "superseded") n.addClass("superseded"); });
  cy.edges().forEach((e) => { if (e.data("status") === "superseded") e.addClass("superseded"); });
  if (g.stats) {
    $("#graph-sub").textContent = `${g.stats.nodes} entities · ${g.stats.edges} relationships · avg degree ${g.stats.avg_degree}`;
  }
  if (nodes.length) cy.fit(undefined, 40);
}

$("#graph-apply").addEventListener("click", applyGraphFilters);

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
  $$(".legend-row").forEach((r) => r.classList.remove("off"));
  hiddenTypes.clear();
  await buildGraph();
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
        const isSup = m.kind === "superseded";
        return `<div class="tl-item">
          <div class="tl-time">${fmtTime(m.created_at)}</div>
          <div class="tl-text">${esc(m.text)}<span class="tl-kind">${esc(m.kind)}</span>
          ${m.confidence ? `<span class="conf">${Math.round(m.confidence * 100)}%</span>` : ""}</div>
        </div>`;
      }).join("")}
    </div>`).join("");
  $("#timeline").innerHTML = html || `<p class="muted">No memories recorded yet.</p>`;
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

  const r = await api("/search", { method: "POST", body: JSON.stringify(body) });
  const ans = $("#search-answer");
  ans.style.display = "block";
  const stLabel = { answered: "known", unknown: "unknown", uncertain: "uncertain" }[r.status] || r.status;
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
}
function closeEntity() {
  $("#entity-panel").classList.remove("open");
  $("#entity-overlay").classList.remove("show");
  currentEntity = null;
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

  const related = d.related.map((r) => `
    <div class="rel-item ${r.status === "superseded" ? "super" : ""}" data-id="${r.other_id}">
      <span style="color:${typeColors[r.other_type] || "#fff"}">●</span>
      <span class="ri-name">${esc(r.other_name)}</span>
      ${badge(r.other_type)}
      <span class="rel-conf">${Math.round((r.confidence || 0.8) * 100)}%</span>
      <span class="ri-rel">${r.direction === "out" ? "→" : "←"} ${esc(r.relation)}</span>
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
    el.addEventListener("click", () => openEntity(el.dataset.id)));
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
    cy.elements().addClass("dim");
    const n = cy.getElementById(String(id));
    n.removeClass("dim");
    n.neighborhood().removeClass("dim");
    cy.animate({ fit: { eles: n.neighborhood().add(n), padding: 80 }, duration: 400 });
    closeEntity();
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
  $("#db-path").textContent = "Database: " + s.db_path;
  $("#ollama-info").innerHTML = s.ollama_available
    ? `<p class="hint">Ollama is <span style="color:var(--ok)">online</span>.</p>
       <p class="hint">Installed models: ${s.models_installed.map(esc).join(", ") || "none"}</p>`
    : `<p class="hint">Ollama is <span style="color:var(--danger)">offline</span> — running the built-in rule-based extractor.</p>
       <p class="hint">Start it with <code>ollama serve</code> and pull <code>qwen3:0.6b</code> + <code>nomic-embed-text</code>.</p>`;
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
  })});
  toast("Memory behavior saved");
});

$("#reset-btn").addEventListener("click", async () => {
  if (!confirm("Wipe ALL entities, relationships, memories and messages?")) return;
  await api("/reset", { method: "POST" });
  toast("All data cleared");
  location.reload();
});

$("#demo-btn").addEventListener("click", async () => {
  await api("/demo", { method: "POST" });
  toast("Demo data loaded");
  loadDashboard(); buildGraph(); loadMemory();
});

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

$("#import-merge").addEventListener("click", async () => {
  const data = $("#import-data").value.trim();
  if (!data) return;
  try {
    const r = await api("/import", { method: "POST", body: JSON.stringify({ data, mode: "merge" }) });
    $("#import-status").textContent = r.ok
      ? `Merged: ${r.entities_created} created, ${r.entities_merged} merged, ${r.relationships_added} relationships.`
      : "Error: " + r.error;
    if (r.ok) { loadDashboard(); buildGraph(); }
  } catch (e) { $("#import-status").textContent = "Error: " + e.message; }
});

$("#import-replace").addEventListener("click", async () => {
  const data = $("#import-data").value.trim();
  if (!data) return;
  if (!confirm("Replace the ENTIRE database with this import? This wipes all current data.")) return;
  try {
    const r = await api("/import", { method: "POST", body: JSON.stringify({ data, mode: "replace" }) });
    $("#import-status").textContent = r.ok
      ? `Replaced: ${r.entities_created} entities imported.`
      : "Error: " + r.error;
    if (r.ok) { loadDashboard(); buildGraph(); loadMemory(); }
  } catch (e) { $("#import-status").textContent = "Error: " + e.message; }
});

$("#backup-now").addEventListener("click", async () => {
  const r = await api("/backup", { method: "POST" });
  $("#backup-status").textContent = r.ok
    ? `Backup created at ${r.path} (db: ${r.db}, json: ${r.export_json}, md: ${r.export_md})`
    : "Backup failed";
});

async function loadBackupStatus() {
  try {
    const s = await api("/backup/status");
    if (s.count) {
      $("#backup-status").textContent = `Last backup: ${s.last_backup_at || "—"} · ${s.count} total · ${s.backup_dir}`;
    }
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
   Boot
   ========================================================================== */
async function boot() {
  refreshStatus();
  await loadChatHistory();
  await buildGraph();
  await loadDashboard();
  await loadSettings();
  loadBackupStatus();
  loadSummarizeCandidates();
  showView("dashboard");
  setInterval(refreshStatus, 15000);
}
boot();
