import streamlit as st
from app.ingestion import scrape_website, extract_text_from_pdf, create_chunks
from app.vector_store import add_documents, search
from app.rag_chain import answer

def render_app():
    st.set_page_config(
        page_title="Local RAG Assistant", 
        layout="wide",
    )

    st.title("Local RAG Assistant")
    st.write("Upload a PDF or enter a website URL to index its content, then ask questions about it using a local LLM.")

    url=st.text_input("Enter website URL")
    if st.button("Index URL"):
        with st.spinner("Processing URL..."):
            text=scrape_website(url)
            chunks=create_chunks(text, origin=url)
            message=add_documents(chunks)
            st.success(message)

    uploaded_file=st.file_uploader("Upload a PDF document", type=["pdf"])
    if uploaded_file and st.button("Index PDF"):
        with st.spinner("Processing PDF..."):
            text=extract_text_from_pdf(uploaded_file)
            chunks=create_chunks(text, origin=uploaded_file.name)
            message=add_documents(chunks)
            st.success(message)

    query=st.text_input("Ask a question based on stored content:")
    if query:
        results=search(query)
        if not results:
            st.warning("No content has been indexed yet.")
        else:
            response=answer(query, results)
            st.subheader("Answer")
            st.write(response)