from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
import os

from .models import Question, Answer
from ..services.ask import load_qa_chain
from ..services.vector_store import create_vectorstore
from ..utils.config import PDF_PATH, DB_DIR
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global qa_chain
    if not os.path.exists(DB_DIR):
        print("📦 No se encontró base de vectores. Creando...")
        create_vectorstore(PDF_PATH)
    else:
        print("📦 Base de vectores encontrada.")
    qa_chain = load_qa_chain()
    yield
    # Shutdown
    qa_chain = None

app = FastAPI(
    title="Estadística PDF QA API",
    description="API para hacer preguntas sobre el PDF de estadística",
    version="1.0.0",
    lifespan=lifespan
)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://slozanoa.lat",
    "http://144.91.91.7:8001",
    "https://next-chat-rag.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

qa_chain = None

@app.post("/ask", response_model=Answer)
async def ask_question(question: Question):
    global qa_chain
    if not qa_chain:
        raise HTTPException(status_code=503, detail="QA chain no está inicializado")

    try:
        result = qa_chain.invoke({"query": question.query})
        return {
            "result": result["result"],
            "sources": [
                {
                    "content": doc.page_content[:300],
                    "page": doc.metadata.get("page", 0) + 1
                } 
                for doc in result["source_documents"]
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))