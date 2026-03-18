from notion_client import Client
from config.settings import settings

notion = Client(auth=settings.notion_api_key)

def push_briefing_to_notion(client_id: str, founder_name: str, briefing_text: str, week_of: str) -> str:
    props = {
        "Title": {"title": [{"text": {"content": f"Regulatory Briefing — {founder_name} — {week_of}"}}]},
        "Client": {"rich_text": [{"text": {"content": client_id}}]},
        "Week Of": {"rich_text": [{"text": {"content": week_of}}]},
        "Status": {"select": {"name": "New"}},
    }
    page = notion.pages.create(
        parent={"database_id": settings.notion_database_id},
        properties=props,
        children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": briefing_text}}]},
            }
        ],
    )
    return page["url"]
