import uuid

from app.db.supabase_client import supabase


def create_chat(project_id, title):

    chat_id = str(uuid.uuid4())

    response = supabase.table("chats").insert({
        "id": chat_id,
        "project_id": project_id,
        "title": title
    }).execute()

    return response.data


def update_chat_title(chat_id, title):

    response = supabase.table("chats") \
        .update({"title": title}) \
        .eq("id", chat_id) \
        .execute()

    return response.data


def get_project_chats(project_id):

    response = supabase.table("chats") \
        .select("*") \
        .eq("project_id", project_id) \
        .order("created_at", desc=True) \
        .execute()

    return response.data