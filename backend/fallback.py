"""Local, offline fallbacks.

When Ollama is not available (or not yet installed), Second Brain keeps
working using a small deterministic rule-based extractor and a hashed n-gram
embedding. This keeps the "brain grows itself" experience intact for demos
and first-run, and makes the app 100% functional with zero external services.
"""
import hashlib
import math
import re

from . import config

# --------------------------------------------------------------------------
# Fallback embedding: hashed character 3-grams -> 256-dim unit vector.
# --------------------------------------------------------------------------

_EMBED_DIM = 256


def fallback_embed(text):
    text = text.lower()
    vec = [0.0] * _EMBED_DIM
    grams = set()
    for n in (3, 4):
        for i in range(len(text) - n + 1):
            grams.add(text[i:i + n])
    for w in re.findall(r"[a-z0-9']+", text):
        grams.add(w)
    for g in grams:
        h = int.from_bytes(hashlib.md5(g.encode()).digest()[:4], "big")
        vec[h % _EMBED_DIM] += 1.0
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


# --------------------------------------------------------------------------
# Naming helpers
# --------------------------------------------------------------------------

# lower key -> canonical display name for known technologies.
TECH = {
    "python": "Python", "react": "React", "next.js": "Next.js", "nextjs": "Next.js",
    "ollama": "Ollama", "javascript": "JavaScript", "typescript": "TypeScript",
    "node.js": "Node.js", "node": "Node.js", "sql": "SQL", "postgresql": "PostgreSQL",
    "postgres": "PostgreSQL", "mysql": "MySQL", "mongodb": "MongoDB",
    "docker": "Docker", "kubernetes": "Kubernetes", "git": "Git", "html": "HTML",
    "css": "CSS", "tailwind": "Tailwind CSS", "tailwindcss": "Tailwind CSS",
    "pytorch": "PyTorch", "tensorflow": "TensorFlow", "fastapi": "FastAPI",
    "django": "Django", "flask": "Flask", "c++": "C++", "c#": "C#", "java": "Java",
    "rust": "Rust", "go": "Go", "golang": "Go", "ruby": "Ruby", "php": "PHP",
    "swift": "Swift", "kotlin": "Kotlin", "linux": "Linux", "windows": "Windows",
    "nginx": "Nginx", "redis": "Redis", "rabbitmq": "RabbitMQ", "graphql": "GraphQL",
    "vue": "Vue.js", "angular": "Angular", "svelte": "Svelte", "numpy": "NumPy",
    "pandas": "pandas", "langchain": "LangChain", "stable diffusion": "Stable Diffusion",
    "machine learning": "Machine Learning", "deep learning": "Deep Learning",
    "artificial intelligence": "Artificial Intelligence", "ai agents": "AI Agents",
    "ai": "AI", "ml": "Machine Learning", "llm": "LLM", "llms": "LLMs",
    "gpt": "GPT", "llama": "Llama", "qwen": "Qwen", "vite": "Vite",
    "webpack": "Webpack", "figma": "Figma", "blender": "Blender", "unity": "Unity",
    "unreal engine": "Unreal Engine", "three.js": "Three.js",
    "react native": "React Native", "electron": "Electron", "tauri": "Tauri",
    "aws": "AWS", "azure": "Azure", "gcp": "GCP", "vercel": "Vercel",
    "netlify": "Netlify", "supabase": "Supabase", "firebase": "Firebase",
    "prisma": "Prisma", "claude": "Claude", "groq": "Groq",
    "hugging face": "Hugging Face", "rag": "RAG", "openai api": "OpenAI API",
    "openai": "OpenAI",
}

_ACRONYMS = {"ai", "ml", "llm", "nlp", "api", "js", "ts", "sql", "http", "html",
             "css", "gpu", "cpu", "vram", "ram", "ui", "ux", "vr", "ar", "os",
             "db", "ide", "ci", "cd", "aws", "gcp", "gpt", "rag", "pdf", "3d",
             "2d", "cli", "sdk", "npm", "json", "xml", "url"}

_STOPWORDS = {"i", "a", "an", "the", "my", "our", "new", "to", "and", "or",
              "for", "with", "using", "that", "which", "this", "it", "in", "on",
              "at", "of", "me", "some", "about", "your", "we", "you", "also",
              "called", "named", "project", "currently", "now", "just",
              "tool", "app", "startup", "site", "bot", "platform",
              "website", "system", "saas", "software", "product", "thing"}


def _title_word(w):
    if w in TECH:
        return TECH[w]
    if w in _ACRONYMS:
        return w.upper()
    if w in ("c++", "c#"):
        return w.upper()
    if w.endswith(".js") or w.endswith(".ts"):
        return w[:-3] + "." + w[-2:].upper()
    return w[:1].upper() + w[1:] if w else w


def canonical_name(phrase):
    """Turn a lowercased, possibly messy phrase into a clean display name."""
    phrase = phrase.strip().replace("_", " ").strip()
    phrase = re.sub(r"\s+", " ", phrase)
    key = phrase.lower().strip().strip(".,!?;:'\"")
    if key in TECH:
        return TECH[key]
    words = [w for w in key.split() if w]
    if not words:
        return ""
    return " ".join(_title_word(w) for w in words)


def clean_phrase(p):
    """Strip leading/trailing stopwords and trailing 'and'/conjunctions."""
    p = p.strip().strip(".,!?;:'\"()")
    words = p.split()
    while words and words[0].lower() in _STOPWORDS:
        words = words[1:]
    while words and (words[-1].lower() in _STOPWORDS or words[-1].lower() in ("and", "or")):
        words = words[:-1]
    return " ".join(words)


# --------------------------------------------------------------------------
# Fallback extractor
# --------------------------------------------------------------------------

def extract_with_rules(text):
    entities, relationships, stops = [], [], []
    used_names = set()

    def add_stop(source, target, relation):
        stops.append({"source": source, "target": target, "relation": relation})

    def add(name, etype, desc="", conf=0.75):
        canon = canonical_name(name)
        key = canon.lower()
        if not canon or len(canon) < 2 or key in used_names or key in ("user",):
            return None
        used_names.add(key)
        entities.append({"name": canon, "type": etype, "description": desc,
                         "confidence": conf})
        return canon

    def add_rel(source, target, relation, conf=0.75):
        if not source or not target or source.lower() == target.lower():
            return
        relationships.append({"source": source, "target": target,
                              "relation": relation, "confidence": conf})

    t = text.lower()
    orig = text  # original casing, for proper-noun detection
    # Normalize multiword verbs/phrases so regexes stay simple.
    for a, b in (("working on", "work_on"), ("works on", "work_on"), ("work on", "work_on"),
                 ("is built with", "built_with"), ("is powered by", "powered_by"),
                 ("is built on", "built_with"), ("built on", "built_with"),
                 ("built with", "built_with"), ("powered by", "powered_by"),
                 ("interested in", "interested_in"), ("picking up", "picking_up"),
                 ("curious about", "curious_about"), ("diving into", "diving_into"),
                 ("passionate about", "passionate_about"), ("is learning", "is_learning")):
        t = t.replace(a, b)

    # ---- 1. Project detection -------------------------------------------
    projects = []  # canonical names
    generic_nouns = {"tool", "app", "project", "startup", "site", "game", "bot",
                     "platform", "website", "system", "saas", "software", "product"}
    art = r"(?:\b(?:a|an|my|our|the|new)\s+)?"
    patterns = [
        # "I created/built a tool called Aurora"
        r"\b(?:i|we)\s+(?:created|built|made|started|launched|developed|wrote|am building|am making)\s+"
        + art + r"(?:project|tool|app|startup|site|game|bot|platform|saas|website|system)?\s*(?:called|named)\s+"
        r"['\"]?([a-z0-9][a-z0-9 .\-]{0,24}?)(?=\s+(?:for|to|with|using|that|which|and|or|,|\.)|$)",
        # "my new project Nebula ..."
        r"(?:\b(?:my|our|a|the|new|side|personal|own)\s+){0,3}project\b\s+(?:called|named)?\s*['\"]?([a-z0-9][a-z0-9 .\-]{0,24}?)['\"]?(?=\s+(?:uses|use|using|built_with|that|which|is|for|to|and|with|powered_by|runs_on|runs|,|\.|$))",
        r"\bproject\s+(?:called|named)\s+['\"]?([a-z0-9][a-z0-9 .\-]{0,24}?)['\"]?",
        r"\b(?:called|named)\s+['\"]?([a-z0-9][a-z0-9 .\-]{0,24}?)['\"]?\s+(?:a|an|my|our|the)?\s*(?:project|app|tool|startup|site|game|bot|platform)\b",
        # "I created Aurora"
        r"\b(?:i|we)\s+(?:created|built|made|started|launched|developed|wrote|am building|am making)\s+"
        + art + r"['\"]?([a-z0-9][a-z0-9 .\-]{0,24}?)['\"]?(?=\s+(?:that|which|using|with|and|for|to|,|\.|$))",
    ]
    for pat in patterns:
        for m in re.finditer(pat, t):
            cand = clean_phrase(m.group(1))
            key = canonical_name(cand).lower()
            if (cand and len(key) > 2 and key not in TECH and key not in generic_nouns
                    and not re.fullmatch(r"(that|which|is|for|to|and|with|a|an|the|it|my|new|i|we)", cand)):
                canon = add(cand, "project", f"Project: {canonical_name(cand)}")
                if canon:
                    projects.append(canon)

    # ---- 2. "X uses Y" (X must be a known project or the user) ----------
    for proj in projects:
        for m in re.finditer(re.escape(proj.lower()) + r"\s+(?:uses|use|using|built_with|powered_by|runs_on|relies_on)\s+(.+)", t):
            rest = re.split(r"[.!?](?=\s|$)", m.group(1))[0]
            for part in re.split(r",\s*|\s+and\s+|\s+or\s+", rest):
                item = clean_phrase(part)
                key = canonical_name(item).lower()
                if key and (key in TECH or item):
                    tg = add(item, "technology" if key in TECH else "concept",
                             f"Technology: {canonical_name(item)}" if key in TECH else "")
                    add_rel(proj, tg, "uses")

    # "I/we use X"
    for m in re.finditer(r"\b(?:i|we)\s+(?:use|using|am using)\s+([a-z0-9 .+#/'-]{1,24}?)(?=\s+(?:and|or|for|to|with|,)|\.|$)", t):
        item = clean_phrase(m.group(1))
        key = canonical_name(item).lower()
        if key in TECH:
            tg = add(item, "technology", f"Technology: {canonical_name(item)}")
            add_rel("User", tg, "uses")

    # Proper-noun subject + "uses": "Nebula uses Ollama." (referring to a
    # previously-mentioned project/technology by name). Operates on the
    # ORIGINAL casing so only genuine proper nouns are captured.
    _pronouns = {"he", "she", "they", "it", "this", "that", "who", "which",
                 "there", "here", "one", "we", "you"}
    for m in re.finditer(r"\b([A-Z][A-Za-z0-9.]*(?:\s+[A-Z][A-Za-z0-9.]*){0,3})\s+(?:uses|use|using)\s+(.+)", orig):
        subj = m.group(1).strip()
        subj_key = canonical_name(subj).lower()
        if not subj_key or subj_key in _pronouns or subj_key in _STOPWORDS or subj_key == "user":
            continue
        rest = re.split(r"[.!?](?=\s|$)", m.group(2))[0]
        for part in re.split(r",\s*|\s+and\s+|\s+or\s+", rest):
            item = clean_phrase(part)
            key = canonical_name(item).lower()
            if not key:
                continue
            s = add(subj, "technology" if subj_key in TECH else "project",
                    f"Project: {canonical_name(subj)}" if subj_key not in TECH else "")
            tg = add(item, "technology" if key in TECH else "concept",
                     f"Technology: {canonical_name(item)}" if key in TECH else "")
            add_rel(s, tg, "uses")

    # ---- 3. learning / interested / wants -------------------------------
    for m in re.finditer(r"(?<!machine )(?<!deep )(?<!reinforcement )(?<!active )(?<!imitation )(?<!few-shot )(?<!zero-shot )(?:learning|learn|studying|picking_up)\s+(?:a bit of\s+)?([a-z0-9 .+#/'-]{1,24}?)(?=\s+(?:and|or|to|for|because|since|so|right now|currently|these days|,)|\.|$)", t):
        item = clean_phrase(m.group(1))
        key = canonical_name(item).lower()
        if key and key not in ("i", "me"):
            e = add(item, "technology" if key in TECH else "topic")
            add_rel("User", e, "learning")

    for m in re.finditer(r"(?:interested_in|curious_about|fascinated by|passionate_about|really into|into)\s+(?:building\s+)?([a-z0-9 .+#/'-]{1,28}?)(?=\s+(?:and|or|to|for|because|,)|\.|$)", t):
        item = clean_phrase(m.group(1))
        key = canonical_name(item).lower()
        if key and key not in ("i", "me"):
            e = add(item, "interest" if key not in TECH else "technology")
            add_rel("User", e, "interested_in")

    for m in re.finditer(r"(?:want to|wants to|planning to|plan to|aiming to|would like to|hoping to|going to)\s+(build|create|make|use|learn|start|try|do|develop|work_on|explore)\s+(?:\b(?:a|an|my|the|new)\s+)?([a-z0-9 .+#/'-]{1,28}?)(?=\s+(?:and|or|for|to|because|with|using|,)|\.|$)", t):
        verb, item = m.group(1), clean_phrase(m.group(2))
        key = canonical_name(item).lower()
        if key and key not in ("i", "me"):
            e = add(item, "technology" if key in TECH else "concept")
            rel = "learning" if verb == "learn" else "wants"
            add_rel("User", e, rel)

    # ---- 4. people ------------------------------------------------------
    last_person = None
    for m in re.finditer(r"(?:my friend|my colleague|my partner|i met|i know|met someone called)\s+([a-z][a-z0-9 .\-]{1,24}?)(?=[,.;!]|\s+(?:who|and|,|\.|$))", t):
        p = add(m.group(1).strip(), "person")
        if p:
            last_person = p
        add_rel("User", p, "knows")

    # ---- 5. people working on / learning things ------------------------
    for m in re.finditer(r"\b([a-z][a-z0-9 .\-]{1,24}?)\s+(?:work_on|is_learning|studies)\s+([a-z0-9 .+#/'-]{1,24}?)(?=[,.;]|\s+(?:and|or|for|to|with|,|\.|$))", t):
        subj, obj = clean_phrase(m.group(1)), clean_phrase(m.group(2))
        subj_key = canonical_name(subj).lower()
        obj_key = canonical_name(obj).lower()
        if subj.lower() in ("i", "we", "they", "he", "she", "you"):
            if subj.lower() in ("he", "she", "they") and last_person:
                tg = add(obj, "technology" if obj_key in TECH else "topic")
                add_rel(last_person, tg, "works_on")
            continue
        if not subj_key or not obj_key:
            continue
        s = add(subj, "person")
        if s:
            last_person = s
        tg = add(obj, "technology" if obj_key in TECH else "topic")
        add_rel(s, tg, "works_on")

    # ---- 6. preferences / location / organization ------------------------
    for m in re.finditer(r"\b(?:i|we)\s+(?:prefer|prefers|really like|favorite language is|favourite language is)\s+([a-z0-9 .+#/'-]{1,24}?)(?=\s+(?:and|or|over|for|to|with|,)|\.|$)", t):
        item = clean_phrase(m.group(1))
        key = canonical_name(item).lower()
        if key and key not in ("i", "me"):
            e = add(item, "technology" if key in TECH else "preference")
            add_rel("User", e, "prefers", conf=0.9)

    for m in re.finditer(r"\b(?:i|we)\s+(?:live in|live at|am based in|are based in|moved to)\s+([a-z][a-z0-9 .\-]{1,24}?)(?=[,.;]|\s+(?:and|or|,|\.)|$)", t):
        loc = add(m.group(1).strip(), "location")
        add_rel("User", loc, "lives_in")

    for m in re.finditer(r"\b(?:i|we)\s+(?:work at|work for|am employed at)\s+([a-z][a-z0-9 .\-]{1,24}?)(?=[,.;]|\s+(?:and|or|,|\.)|$)", t):
        org = add(m.group(1).strip(), "organization")
        add_rel("User", org, "works_at")

    # ---- 7. negation / stopped (stale facts -> supersede) ---------------
    neg = r"(?:i|we)?\s*(?:stopped|no longer|quit|gave up on|dropped|not anymore|don't|dont|do not)\s*"
    for m in re.finditer(neg + r"(?:learning|studying|using|working on|working_on|practicing)\s+([a-z0-9 .+#/'-]{1,24}?)(?=[,.;]|\s+(?:and|or|for|to|because|with|,)|\.|$)", t):
        item = clean_phrase(m.group(1))
        canon = canonical_name(item)
        key = canon.lower()
        if not key:
            continue
        # Ensure the entity exists so it can be referenced, but reference by
        # canonical name (works whether or not `add` created it).
        add(item, "technology" if key in TECH else "concept")
        add_stop("User", canon, "learning")

    for m in re.finditer(r"(?:switched|switching)\s+(?:from\s+)?([a-z0-9 .+#/'-]{1,24}?)\s+to\s+([a-z0-9 .+#/'-]{1,24}?)(?=[,.;]|\s+(?:and|or|for|to|because|with|,)|\.|$)", t):
        old, new = clean_phrase(m.group(1)), clean_phrase(m.group(2))
        old_canon, new_canon = canonical_name(old), canonical_name(new)
        old_key, new_key = old_canon.lower(), new_canon.lower()
        if old_key and new_key:
            add(old, "technology" if old_key in TECH else "concept")
            ne = add(new, "technology" if new_key in TECH else "concept")
            # "switched from X to Y" -> stop using/learning X, prefer Y.
            add_stop("User", old_canon, "uses")
            add_stop("User", old_canon, "learning")
            if ne:
                add_rel("User", ne, "prefers", conf=0.9)

    # ---- 8. bare technology mentions (attach as interests if orphaned) ---
    existing_targets = {r["target"].lower() for r in relationships}
    claimed = []  # (start, end) spans already covered by a longer term
    for key in sorted(TECH, key=len, reverse=True):
        canon = TECH[key]
        for m in re.finditer(r"(?<![a-z0-9])" + re.escape(key) + r"(?![a-z0-9])", t):
            if any(m.start() < end and m.end() > start for start, end in claimed):
                continue
            claimed.append((m.start(), m.end()))
            if canon.lower() in used_names or canon.lower() in existing_targets:
                continue
            add(canon, "technology", f"Technology: {canon}")
            add_rel("User", canon, "interested_in")
            existing_targets.add(canon.lower())

    # ---- de-duplicate relationships --------------------------------------
    seen_rel, dedup = set(), []
    for r in relationships:
        k = (r["source"].lower(), r["target"].lower(), r["relation"])
        if k not in seen_rel and r["source"].lower() != r["target"].lower():
            seen_rel.add(k)
            dedup.append(r)

    # de-duplicate stops
    seen_stop, dedup_stop = set(), []
    for s in stops:
        k = (s["source"].lower(), s["target"].lower(), s["relation"])
        if k not in seen_stop and s["source"].lower() != s["target"].lower():
            seen_stop.add(k)
            dedup_stop.append(s)

    return {"entities": entities, "relationships": dedup, "stops": dedup_stop}


def is_trivial(text):
    """Heuristic for small-talk that should never enter the brain."""
    t = text.strip().lower().strip(".,!? ")
    if len(t) < 3:
        return True
    if t in config.TRIVIAL_PATTERNS:
        return True
    if len(t.split()) == 1 and not re.search(r"[a-z]{4,}", t):
        return True
    return False
