from fastapi import APIRouter, UploadFile, File, Form
import os
import shutil
import tempfile

from app.models.upload_model import UploadResponse

from app.services.pdf_service import extract_text_from_pdf
from app.services.chunk_service import chunk_text
from app.services.embedding_service import generate_embedding
from app.services.storage_service import store_document_chunks

router = APIRouter()

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@router.post("/upload", response_model=UploadResponse)
def upload_pdf(
    project_id: str = Form(...),
    file: UploadFile = File(...)
):

    # Validate PDF
    if file.content_type != "application/pdf":
        return {
            "error": "Only PDF files are allowed"
        }
    
    # Validate file size
    file.file.seek(0, 2)
    
    file_size = file.file.tell()
    
    file.file.seek(0)
    
    if file_size > MAX_FILE_SIZE:
    
        return {
            "error": "File size exceeds 10 MB limit"
        }

    # Save file to a temporary path for processing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        file_path = temp_file.name
        shutil.copyfileobj(file.file, temp_file)

    try:
        # Extract text
        extracted_text = extract_text_from_pdf(file_path)

        # Chunk text
        chunks = chunk_text(extracted_text)
    finally:
        try:
            os.remove(file_path)
        except OSError:
            pass

    embedded_chunks = []

    # Generate embeddings
    for chunk in chunks:

        embedding = generate_embedding(chunk)

        if embedding is None:
            continue;

        embedded_chunks.append({
            "chunk": chunk,
            "embedding": embedding
        })

    # Store chunks
    try:
        store_document_chunks(
            project_id=project_id,
            filename=file.filename,
            chunks=embedded_chunks
        )
    except Exception as e:
        return {
            "error": f"Failed to save document chunks: {e}"
        }

    return UploadResponse(
        message="PDF uploaded successfully",
        project_id=project_id,
        total_chunks=len(chunks)
    )