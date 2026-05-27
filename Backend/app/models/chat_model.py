from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    project_id: str
    chat_id: str