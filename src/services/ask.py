from dotenv import load_dotenv
import os
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from ..utils.config import DB_DIR, MODEL_NAME, MAX_TOKENS, TEMPERATURE

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Por favor, configura la variable de entorno OPENAI_API_KEY en el archivo .env")

def load_qa_chain(persist_directory=DB_DIR):
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)
    vectordb = Chroma(persist_directory=str(persist_directory), embedding_function=embeddings)
    retriever = vectordb.as_retriever()
    llm = ChatOpenAI(
        model="gpt-3.5-turbo", 
        temperature=TEMPERATURE, 
        max_tokens=MAX_TOKENS
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain