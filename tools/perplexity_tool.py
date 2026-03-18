import httpx
from config.settings import settings

PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"

def research_regulatory(query: str) -> str:
    """
    Use Perplexity Sonar to research payer policies, CPT updates,
    prior auth trends, and state mandates for women's health.
    """
    headers = {
        "Authorization": f"Bearer {settings.perplexity_api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a regulatory and reimbursement specialist for women's health tech companies. "
                    "Monitor and summarize: payer medical policy changes, CPT code additions/deletions, "
                    "prior authorization requirement changes, CMS proposed rules, state insurance mandates "
                    "for women's health services, and FDA guidance documents. Always cite the source URL."
                ),
            },
            {"role": "user", "content": query},
        ],
    }
    response = httpx.post(PERPLEXITY_URL, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
