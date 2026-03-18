import httpx
from typing import Optional

CMS_API_BASE = "https://data.cms.gov/data-api/v1/dataset"

# CMS Local Coverage Determinations (LCD) dataset ID
LCD_DATASET_ID = "9767-9767"

def search_lcds(keyword: str, limit: int = 20) -> list[dict]:
    """
    Search CMS Local Coverage Determinations for a keyword.
    Returns LCDs that may affect coverage of a founder's product.
    """
    params = {
        "filter[contractor_name][value]": keyword,
        "size": limit,
        "offset": 0,
    }
    response = httpx.get(
        f"{CMS_API_BASE}/{LCD_DATASET_ID}/data",
        params=params,
        timeout=20,
    )
    response.raise_for_status()
    return response.json().get("data", [])

def search_ncds(keyword: str, limit: int = 10) -> list[dict]:
    """
    Search CMS National Coverage Determinations.
    NCDs are binding across all Medicare contractors.
    """
    NCD_DATASET_ID = "9770-9770"
    params = {"filter[title][value]": keyword, "size": limit}
    response = httpx.get(
        f"{CMS_API_BASE}/{NCD_DATASET_ID}/data",
        params=params,
        timeout=20,
    )
    response.raise_for_status()
    return response.json().get("data", [])
