from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from ..utils.config import PDF_PATH, CHUNK_SIZE, CHUNK_OVERLAP



def load_and_split_pdf(file_path=PDF_PATH):
    loader = PyPDFLoader(str(file_path))
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, 
        chunk_overlap=CHUNK_OVERLAP, 
        separators=["\n", ".", " ", "?", "!", " ", ""]
    )
    docs = text_splitter.split_documents(docs)
    return docs
