from pydantic import BaseModel


class StoreMessageRequest(BaseModel):
    chat_id: str
    role: str
    content: str