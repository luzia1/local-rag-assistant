# Local RAG Assistant

A local Retrieval-Augmented Generation (RAG) application that lets users index PDF documents and website content, then ask questions about it using a local LLM.

## Features

- PDF ingestion and text extraction
- Website scraping and content extraction
- Text chunking with configurable size and overlap
- Semantic search with FAISS
- Local answer generation with Ollama
- Streamlit web interface

## Tech stack

- Python
- LangChain
- FAISS
- Hugging Face embeddings
- Ollama
- Streamlit

## Getting started

1. Install Ollama and pull a model:

```bash
ollama pull mistral
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app/main.py
```

## Project structure

```text
app/
├── main.py
├── config.py
├── ingestion.py
├── vector_store.py
├── rag_chain.py
└── ui.py

storage/
└── faiss_index/

tests/
└── test_ingestion.py
```

## Notes

- The FAISS index is stored locally in `storage/faiss_index/`.
- Add this folder to `.gitignore`; do not commit generated indexes or personal documents.