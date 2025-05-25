from pydantic import BaseModel

class Question(BaseModel):
    query: str

class Source(BaseModel):
    content: str
    page: int

class Answer(BaseModel):
    result: str
    sources: list[Source]