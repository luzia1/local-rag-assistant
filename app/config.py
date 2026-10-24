from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OLLAMA_MODEL = "mistral"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
TOP_K = 3
FAISS_INDEX_DIR = BASE_DIR / "storage" / "faiss_index"