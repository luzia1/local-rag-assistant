from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from app.config import EMBEDDING_MODEL, FAISS_INDEX_DIR, TOP_K

def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def get_vector_store():
    index_file = FAISS_INDEX_DIR / "index.faiss"

    if not index_file.exists():
        return None

    return FAISS.load_local(
            folder_path=FAISS_INDEX_DIR,
            embeddings=get_embeddings(),
            allow_dangerous_deserialization=True,
        )

def add_documents(chunks):
    vector_store = get_vector_store()

    if vector_store is None:
        vector_store=FAISS.from_documents(
            documents=chunks,
            embedding=get_embeddings()
        )
    else:
        vector_store.add_documents(chunks)

    vector_store.save_local(str(FAISS_INDEX_DIR))

    return "Document successfully indexed."

def search(question):
    vector_store = get_vector_store()

    if vector_store is None:
        return []

    results=vector_store.similarity_search(query=question, k=TOP_K)

    return results