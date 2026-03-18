from crewai import Agent
from tools.cms_tool import search_lcds, search_ncds
from tools.perplexity_tool import research_regulatory

PAYER_QUERIES = [
    "UnitedHealthcare medical policy update women's health digital health 2026",
    "Aetna prior authorization requirements digital therapeutics women's health",
    "BCBS coverage policy remote patient monitoring maternal health 2026",
    "CMS Medicare Advantage women's health coverage policy changes 2026",
    "Medicaid coverage women's health tech state policy updates",
    "prior authorization burden digital health women's health payer trends 2026",
]

payer_monitor_agent = Agent(
    role="Payer Policy Intelligence Analyst",
    goal=(
        "Monitor medical policy changes, prior authorization requirement updates, "
        "and coverage decisions from major payers — CMS, UnitedHealthcare, Aetna, "
        "BCBS — relevant to each founder's product category. Flag both coverage "
        "expansions (opportunities) and new prior auth requirements (barriers)."
    ),
    backstory=(
        "You are a managed care and payer relations expert who reads payer medical "
        "policies so founders don't have to. You know how to spot a coverage expansion "
        "before it's widely known, and how to warn founders when a payer is quietly "
        "tightening prior auth for their product category."
    ),
    tools=[search_lcds, search_ncds, research_regulatory],
    verbose=True,
    allow_delegation=False,
)
