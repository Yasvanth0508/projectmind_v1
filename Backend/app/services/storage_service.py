from app.db.supabase_client import supabase


def store_document_chunks(project_id, filename, chunks):

    documents_to_insert = []

    for chunk_data in chunks:
        embedding = chunk_data.get("embedding")
        chunk_text = chunk_data.get("chunk")

        if not chunk_text or embedding is None:
            continue

        document = {
            "project_id": project_id,
            "content": chunk_text,
            "embedding": list(embedding),
            "metadata": {
                "filename": filename
            }
        }

        documents_to_insert.append(document)

    if not documents_to_insert:
        raise ValueError("No valid document chunks to insert. Please confirm your PDF content and embedding generation.")

    response = supabase.table("documents").insert(documents_to_insert).execute()

    if hasattr(response, 'error') and response.error:
        raise RuntimeError(f"Supabase insert failed: {response.error}")

    return response.data