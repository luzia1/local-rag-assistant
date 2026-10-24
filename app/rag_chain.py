from langchain_ollama import OllamaLLM
from app.config import OLLAMA_MODEL
from app.vector_store import search

def get_llm():
    return OllamaLLM(model=OLLAMA_MODEL)

def answer(query, results):

    context="\n\n".join(
            result.page_content
            for result in results
        )
    
    prompt=f"""
    Based on the following context, answer the question.
    
    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    return get_llm().invoke(prompt)