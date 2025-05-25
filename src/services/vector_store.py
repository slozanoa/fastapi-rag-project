from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from .ingestor import load_and_split_pdf
from ..utils.config import DB_DIR, MODEL_NAME

def create_vectorstore(pdf_path):
    docs = load_and_split_pdf(pdf_path)
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=str(DB_DIR)
    )
    vectorstore.persist()
    return vectorstore