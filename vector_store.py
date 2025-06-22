from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def build_vector_store(text_chunks):
    embeddings = HuggingFaceEmbeddings()
    db = Chroma.from_texts(text_chunks, embedding=embeddings)
    return db

def semantic_search(db, query, k=3):
    return db.similarity_search(query, k=k) 