from fastapi import APIRouter
from ask import load_qa_chain
from api.models import Question, Answer

router = APIRouter()
qa_chain = load_qa_chain()

@router.post("/ask", response_model=Answer)
async def ask_question(question: Question):
    result = qa_chain.invoke({"query": question.query})
    return {"result": result["result"]}