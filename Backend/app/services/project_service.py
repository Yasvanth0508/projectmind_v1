from app.db.supabase_client import supabase


def create_project(project_id, project_name):

    response = supabase.table("projects").insert({
        "id": project_id,
        "name": project_name
    }).execute()

    return response.data


def get_all_projects():

    response = supabase.table("projects") \
        .select("*") \
        .order("created_at", desc=True) \
        .execute()

    return response.data