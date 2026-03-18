import httpx
from datetime import datetime, timedelta

FEDERAL_REGISTER_API = "https://www.federalregister.gov/api/v1/documents.json"

def search_federal_register(
    terms: list[str],
    days_back: int = 14,
    agencies: list[str] = None,
) -> list[dict]:
    """
    Search Federal Register for recent FDA/CMS guidance documents.
    agencies: e.g. ['food-and-drug-administration', 'centers-for-medicare-medicaid-services']
    """
    agencies = agencies or [
        "food-and-drug-administration",
        "centers-for-medicare-medicaid-services",
    ]
    since_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    params = {
        "conditions[term]": " ".join(terms),
        "conditions[agencies][]": agencies,
        "conditions[publication_date][gte]": since_date,
        "fields[]": ["title", "abstract", "publication_date", "html_url", "agencies"],
        "per_page": 20,
        "order": "newest",
    }
    response = httpx.get(FEDERAL_REGISTER_API, params=params, timeout=20)
    response.raise_for_status()
    return response.json().get("results", [])
