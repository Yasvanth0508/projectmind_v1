from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

project_root = Path(__file__).resolve().parents[1]
dotenv_path = project_root / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path=dotenv_path)

def _parse_list(value: str | None, default: list[str] = None) -> list[str]:
    if default is None:
        default = ["*"]
    if value is None:
        return default
    items = [item.strip() for item in value.split(",") if item.strip()]
    return items or default

@dataclass
class Settings:
    environment: str = os.getenv("ENVIRONMENT", "development")
    log_level: str = os.getenv("LOG_LEVEL", "info")
    backend_host: str = os.getenv("BACKEND_HOST", "0.0.0.0")
    backend_port: int = int(os.getenv("BACKEND_PORT", "8000"))
    cors_origins: list[str] = field(default_factory=lambda: _parse_list(os.getenv("CORS_ORIGINS", "*")))
    supabase_url: str = os.getenv("SUPABASE_URL", "")
    supabase_key: str = os.getenv("SUPABASE_KEY", "")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

    def validate(self) -> None:
        if not self.supabase_url or not self.supabase_key:
            raise RuntimeError("SUPABASE_URL and SUPABASE_KEY must be set in .env or environment variables.")
        if not self.gemini_api_key:
            raise RuntimeError("GEMINI_API_KEY must be set in .env or environment variables.")

settings = Settings()
settings.validate()
