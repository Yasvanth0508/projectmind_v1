from pydantic import BaseModel


class CreateChatRequest(BaseModel):
    project_id: str
    title: str


class UpdateChatTitleRequest(BaseModel):
    chat_id: str
    title: str


class ChatResponse(BaseModel):
    id: str
    project_id: str
    title: str