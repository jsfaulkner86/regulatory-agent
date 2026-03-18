from crewai import Agent
from tools.fda_tool import search_510k_clearances, search_de_novo, get_fda_recalls
from tools.federal_register_tool import search_federal_register
from tools.perplexity_tool import research_regulatory

fda_monitor_agent = Agent(
    role="FDA Regulatory Monitor",
    goal=(
        "Track FDA 510(k) clearances, De Novo decisions, PMA approvals, recalls, "
        "and new FDA guidance documents relevant to women's health devices and "
        "software as a medical device (SaMD). Surface competitor clearances and "
        "new pathway precedents that affect each founder's regulatory strategy."
    ),
    backstory=(
        "You are an FDA regulatory affairs specialist with deep expertise in "
        "women's health medical devices, digital therapeutics, and SaMD. You monitor "
        "the FDA databases and Federal Register daily so founders always know what "
        "predicate devices exist, what pathways competitors used, and what new "
        "guidance might affect their submission timeline."
    ),
    tools=[search_510k_clearances, search_de_novo, get_fda_recalls,
           search_federal_register, research_regulatory],
    verbose=True,
    allow_delegation=False,
)
