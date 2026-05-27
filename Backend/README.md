# Backend Deployment Guide

## Setup

1. Copy the environment example:
   ```bash
   cd Backend
   cp .env.example .env
   ```
2. Fill in the values in `.env`:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
   - `GEMINI_API_KEY`
   - Optional: `CORS_ORIGINS`, `BACKEND_PORT`, `LOG_LEVEL`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run locally

```bash
cd Backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then open `http://localhost:8000/docs` for the FastAPI docs.

## What changed for deployment readiness

- Added centralized config in `app/config.py`
- Removed multiple ad hoc `.env` loads across service modules
- Added `.env.example` and `.gitignore`
- Updated upload handling to use temporary files instead of a persistent `uploads/` folder

## Required environment variables

- `SUPABASE_URL`
- `SUPABASE_KEY`
- `GEMINI_API_KEY`
- `CORS_ORIGINS` (default: `*`)
- `BACKEND_HOST` (default: `0.0.0.0`)
- `BACKEND_PORT` (default: `8000`)

## Deployment platforms

### Render
1. Create a new Web Service.
2. Set `Root Directory` to `Backend`.
3. Use build command:
   ```bash
   pip install -r requirements.txt
   ```
4. Use start command:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
5. Add environment variables in Render settings.

### Railway
1. Create a new Python service and connect your repo.
2. Set the start command to:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
3. Add environment variables under service settings.

### Fly.io
1. Install the Fly CLI and run `fly launch` in `Backend`.
2. Configure `Dockerfile` or use the Python builder.
3. Deploy with:
   ```bash
   fly deploy
   ```
4. Set secrets using:
   ```bash
   fly secrets set SUPABASE_URL=... SUPABASE_KEY=... GEMINI_API_KEY=...
   ```

## Notes for production

- Do not commit `.env`
- Use secret stores or platform environment variables to keep credentials safe
- Local file uploads are temporary; for production, use a remote storage service if you need persistence
