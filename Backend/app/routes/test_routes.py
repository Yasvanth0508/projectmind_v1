from fastapi import APIRouter
from app.models.chat_model import ChatRequest

router = APIRouter()

@router.get("/")
def home():
    return {"message": "RAG Backend Running Successfully"}

@router.get("/health")
def health_check():
    return {"status": "healthy"}
