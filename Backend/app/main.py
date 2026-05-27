from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routes.project_routes import router as project_router
from app.routes.test_routes import router as test_router
from app.routes.upload_routes import router as upload_router
from app.routes.chat_routes import router as chat_router
from app.routes.chat_session_routes import router as chat_session_router
from app.routes.message_routes import router as message_router
from app.routes.stream_chat_routes import (
    router as stream_chat_router
)

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,

    allow_origins=settings.cors_origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


app.include_router(test_router)
app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(project_router)
app.include_router(chat_session_router)
app.include_router(message_router)
app.include_router(stream_chat_router)