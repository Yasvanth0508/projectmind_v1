from pydantic import BaseModel


class UploadResponse(BaseModel):
    message: str
    project_id: str
    total_chunks: int