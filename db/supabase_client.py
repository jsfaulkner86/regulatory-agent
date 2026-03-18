from supabase import create_client, Client
from config.settings import settings

supabase: Client = create_client(settings.supabase_url, settings.supabase_key)

def upsert_regulatory_item(item: dict) -> dict:
    result = (
        supabase.table("regulatory_items")
        .upsert(item, on_conflict="item_id")
        .execute()
    )
    return result.data

def get_existing_item_ids() -> list[str]:
    result = supabase.table("regulatory_items").select("item_id").execute()
    return [row["item_id"] for row in result.data]

def save_briefing(briefing: dict) -> dict:
    result = supabase.table("regulatory_briefings").insert(briefing).execute()
    return result.data
