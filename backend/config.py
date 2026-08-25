"""Configuration for Second Brain.

All runtime options are driven by environment variables (or the Settings UI,
which persists to the SQLite settings table). Nothing here should need to be
edited by hand — change models via .env / Settings instead of touching code.
"""
import os

from . import paths

# ---- Paths ---------------------------------------------------------------
BASE_DIR = str(paths.app_root())
FRONTEND_DIR = str(paths.frontend_dir())


def _load_dotenv():
    """Load a local .env if present. Does not override already-set env vars."""
    for candidate in (
        os.path.join(BASE_DIR, ".env"),
        os.path.join(BASE_DIR, "backend", ".env"),
        os.path.join(str(paths.app_root()), ".env"),
    ):
        if not os.path.isfile(candidate):
            continue
        try:
            with open(candidate, encoding="utf-8") as fh:
                for raw in fh:
                    line = raw.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip().strip("\"'")
                    if key and key not in os.environ:
                        os.environ[key] = value
        except OSError:
            continue


_load_dotenv()

# Persistent DB path. Never a PyInstaller temp extract directory.
DB_PATH = str(paths.resolve_db_path())

# ---- AI / model configuration (the "replaceable LLM" requirement) --------
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")

# The small local LLM used for extraction (and optional RAG answers).
DEFAULT_LLM_MODEL = os.environ.get("OLLAMA_MODEL", "qwen3:0.6b")

# Embedding model for semantic / vector memory search.
DEFAULT_EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "nomic-embed-text")

# How long to wait for Ollama (seconds).
OLLAMA_TIMEOUT = float(os.environ.get("OLLAMA_TIMEOUT", "120"))

# Thresholds (defaults — overridable at runtime via Settings) --------------
DEFAULT_CONFIDENCE_THRESHOLD = 0.4   # drop entities/relations below this
DEFAULT_MERGE_SIMILARITY = 0.92      # cosine similarity at which entities auto-merge
VECTOR_SEARCH_K = 8                  # top-k vector results
SHORT_TERM_CONTEXT_TURNS = 10        # recent messages fed as conversation context
MAX_CHAT_CHARS = 16000               # hard cap on a single chat / extract payload
MAX_EXTRACT_CHARS = 8000             # extractor window (head of the message)
DEFAULT_AUTO_BACKUP_HOURS = 24.0     # 0 disables scheduled local backups

# --------------------------------------------------------------------------
# Memory types (categories). Kept rich but non-forcing: the extractor only
# assigns a type it is confident about, otherwise falls back to "concept".
# --------------------------------------------------------------------------
ENTITY_TYPES = [
    "person", "project", "technology", "topic",
    "skill", "goal", "interest", "preference", "fact",
    "location", "organization", "concept", "task", "event",
]

# Canonical relationship labels (active voice).
RELATION_TYPES = [
    "learning", "uses", "knows", "likes", "created",
    "interested_in", "related_to", "wants", "works_on",
    "prefers", "works_at", "lives_in", "located_in", "member_of",
]

# Inverse labels -> canonical (triggers source/target swap on import).
RELATION_INVERSE = {
    "being_learned_by": "learning", "learned_by": "learning",
    "used_by": "uses", "known_by": "knows", "liked_by": "likes",
    "created_by": "created", "interest_of": "interested_in",
    "wanted_by": "wants", "worked_on_by": "works_on",
    "preferred_by": "prefers", "employs": "works_at",
    "home_of": "lives_in", "contains": "located_in", "has_member": "member_of",
}

# Synonyms -> canonical (no swap).
RELATION_SYNONYMS = {
    "learning": "learning", "learn": "learning", "is_learning": "learning",
    "studying": "learning", "practicing": "learning",
    "uses": "uses", "use": "uses", "using": "uses", "utilizes": "uses",
    "built_with": "uses", "powered_by": "uses", "relies_on": "uses",
    "knows": "knows", "know": "knows",
    "likes": "likes", "like": "likes", "loves": "likes", "enjoys": "likes",
    "favorite": "likes", "prefers": "prefers", "prefer": "prefers",
    "preference": "prefers", "preferred": "prefers", "favorite_language": "prefers",
    "created": "created", "create": "created", "made": "created",
    "built": "created", "developed": "created", "founded": "created",
    "started": "created", "wrote": "created", "designed": "created",
    "interested_in": "interested_in", "interested": "interested_in",
    "curious_about": "interested_in", "into": "interested_in",
    "related_to": "related_to", "related": "related_to", "associated_with": "related_to",
    "part_of": "related_to", "is_a": "related_to", "connected_to": "related_to",
    "wants": "wants", "want": "wants", "wants_to": "wants", "plans_to": "wants",
    "planning_to": "wants", "aiming_to": "wants", "goal_is": "wants",
    "works_on": "works_on", "work_on": "works_on", "working_on": "works_on",
    "works_with": "works_on", "contributes_to": "works_on",
    "works_at": "works_at", "employed_at": "works_at", "works_for": "works_at",
    "lives_in": "lives_in", "lives at": "lives_in", "based_in": "lives_in",
    "located_in": "located_in", "located at": "located_in", "headquartered_in": "located_in",
    "member_of": "member_of", "belongs_to": "member_of", "part_of_team": "member_of",
}

# Entity type synonyms -> canonical.
TYPE_SYNONYMS = {
    "person": "person", "people": "person", "human": "person", "friend": "person",
    "colleague": "person", "contact": "person", "user": "person",
    "project": "project", "product": "project", "app": "project", "application": "project",
    "startup": "project", "side_project": "project",
    "technology": "technology", "tech": "technology", "tool": "technology",
    "software": "technology", "language": "technology", "framework": "technology",
    "library": "technology", "platform": "technology", "model": "technology",
    "topic": "topic", "subject": "topic", "field": "topic", "domain": "topic",
    "skill": "skill", "ability": "skill", "competence": "skill",
    "goal": "goal", "objective": "goal", "target": "goal", "aim": "goal",
    "fact": "fact", "fact_": "fact",
    "interest": "interest", "hobby": "interest", "passion": "interest",
    "preference": "preference", "pref": "preference",
    "location": "location", "place": "location", "city": "location", "country": "location",
    "organization": "organization", "org": "organization", "company": "organization",
    "team": "organization", "institute": "organization", "university": "organization",
    "concept": "concept", "idea": "concept", "thing": "concept",
    "task": "task", "todo": "task", "action_item": "task",
    "event": "event", "meeting": "event", "conference": "event", "milestone": "event",
}

# Small-talk phrases that should never become permanent knowledge.
TRIVIAL_PATTERNS = {
    "hi", "hello", "hey", "yo", "sup", "hola", "good morning", "good evening",
    "good afternoon", "good night", "how are you", "how are u", "how's it going",
    "whats up", "what's up", "thanks", "thank you", "thx", "ty", "ok", "okay",
    "k", "cool", "nice", "great", "awesome", "yes", "no", "yeah", "nah", "sure",
    "fine", "good", "lol", "lmao", "haha", "hehe", "idk", "idc", "bye", "goodbye",
    "see you", "later", "cya", "got it", "gotcha", "understood", "np", "no problem",
    "welcome", "you're welcome", "sounds good", "will do", "👍", "🙂", "😊", "😂",
    "what time is it", "tell me a joke", "what's the weather", "what is the time",
}

# The user is a first-class entity in the graph.
USER_ENTITY_NAME = "User"
USER_ENTITY_DESCRIPTION = "You — the owner of this Second Brain."

# Colors (frontend maps types to colors; kept here for the legend API).
TYPE_COLORS = {
    "person": "#f472b6", "project": "#22d3ee", "technology": "#34d399",
    "topic": "#a78bfa", "skill": "#2dd4bf", "goal": "#60a5fa",
    "interest": "#fb923c", "preference": "#e879f9", "fact": "#f87171",
    "location": "#4ade80", "organization": "#38bdf8", "concept": "#fbbf24",
    "task": "#94a3b8", "event": "#f472b6",
}
