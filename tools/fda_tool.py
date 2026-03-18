import httpx
from typing import Optional

FDA_DEVICE_API = "https://api.fda.gov/device"

def search_510k_clearances(
    product_code: Optional[str] = None,
    search_term: Optional[str] = None,
    limit: int = 20,
) -> list[dict]:
    """Search FDA 510(k) clearances by product code or search term."""
    query_parts = []
    if product_code:
        query_parts.append(f'product_code:"{product_code}"')
    if search_term:
        query_parts.append(f'device_name:"{search_term}"')
    query = "+AND+".join(query_parts) if query_parts else "device_name:\"women\""

    params = {"search": query, "limit": limit, "sort": "date_received:desc"}
    response = httpx.get(f"{FDA_DEVICE_API}/510k.json", params=params, timeout=20)
    response.raise_for_status()
    return response.json().get("results", [])

def search_de_novo(
    search_term: Optional[str] = None,
    limit: int = 20,
) -> list[dict]:
    """Search FDA De Novo decisions."""
    query = f'device_name:"{search_term}"' if search_term else 'device_name:"health"'
    params = {"search": query, "limit": limit, "sort": "date_received:desc"}
    response = httpx.get(f"{FDA_DEVICE_API}/denovo.json", params=params, timeout=20)
    response.raise_for_status()
    return response.json().get("results", [])

def get_fda_recalls(product_code: str, limit: int = 10) -> list[dict]:
    """Fetch recent FDA recalls for a product code — competitive + safety awareness."""
    params = {"search": f'product_code:"{product_code}"', "limit": limit}
    response = httpx.get(f"{FDA_DEVICE_API}/enforcement.json", params=params, timeout=20)
    response.raise_for_status()
    return response.json().get("results", [])
