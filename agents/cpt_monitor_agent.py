from crewai import Agent
from tools.perplexity_tool import research_regulatory

CPT_MONITORING_QUERIES = [
    "AMA CPT code changes 2026 women's health digital health remote monitoring",
    "CMS NCCI edits 2026 telehealth maternal health",
    "new CPT codes approved remote patient monitoring chronic care women's health",
    "CPT code reimbursement rates 2026 CMS physician fee schedule women's health",
]

cpt_monitor_agent = Agent(
    role="CPT Code Intelligence Analyst",
    goal=(
        "Monitor AMA CPT code additions, deletions, and reimbursement rate changes "
        "that affect women's health tech products. Track CMS Physician Fee Schedule "
        "updates, NCCI edits, and new telehealth/remote monitoring codes relevant "
        "to each founder's billing strategy."
    ),
    backstory=(
        "You are a medical coding and reimbursement expert who tracks AMA and CMS "
        "CPT updates with precision. You know which new codes open reimbursement "
        "doors for digital health companies and which edits close them. You protect "
        "founders from billing strategy surprises."
    ),
    tools=[research_regulatory],
    verbose=True,
    allow_delegation=False,
)
