from crewai import Crew, Task
from agents.fda_monitor_agent import fda_monitor_agent
from agents.cpt_monitor_agent import cpt_monitor_agent, CPT_MONITORING_QUERIES
from agents.payer_monitor_agent import payer_monitor_agent, PAYER_QUERIES
from agents.briefing_agent import briefing_agent, BRIEFING_PROMPT
from db.supabase_client import save_briefing
from delivery.notion_push import push_briefing_to_notion
from delivery.email_briefing import send_regulatory_briefing
from profiles.founder_profiles import FOUNDER_PROFILES
from datetime import datetime
import json

def run_pipeline():
    week_of = datetime.now().strftime("%B %d, %Y")
    print(f"[RegulatoryAgent] Starting weekly run for week of {week_of}")

    for profile in FOUNDER_PROFILES:
        indication = profile["indication"]
        product_category = profile["product_category"]
        fda_pathway = profile["fda_pathway"]
        product_codes = profile.get("product_codes", [])
        cpt_codes = profile.get("cpt_codes_of_interest", [])
        payers = profile.get("key_payers", [])

        fda_task = Task(
            description=(
                f"Monitor FDA activity for a {product_category} in {indication}. "
                f"FDA pathway: {fda_pathway}. Product codes: {product_codes}. "
                f"Find recent 510(k) clearances, De Novo decisions, recalls, and FDA guidance "
                f"documents from the past 14 days relevant to this product."
            ),
            agent=fda_monitor_agent,
            expected_output="List of relevant FDA actions with date, title, decision, and URL.",
        )
        cpt_task = Task(
            description=(
                f"Monitor CPT code changes relevant to: {cpt_codes}. "
                f"Focus on 2026 AMA CPT updates, CMS Physician Fee Schedule, "
                f"and new remote monitoring or telehealth codes for {indication}."
            ),
            agent=cpt_monitor_agent,
            expected_output="Summary of CPT changes with code numbers, change type, and reimbursement impact.",
        )
        payer_task = Task(
            description=(
                f"Monitor payer policy changes from {payers} for a {product_category} "
                f"treating {indication}. Flag coverage expansions, new prior auth requirements, "
                f"and LCD/NCD changes from CMS."
            ),
            agent=payer_monitor_agent,
            expected_output="List of payer policy changes with payer name, change type, effective date, and impact.",
        )
        briefing_task = Task(
            description=(
                f"Synthesize all FDA, CPT, and payer intelligence for {profile['founder_name']} "
                f"at {profile['company']}. Use this structure:\n{BRIEFING_PROMPT}"
            ),
            agent=briefing_agent,
            expected_output="A structured weekly regulatory briefing in HTML format.",
        )

        crew = Crew(
            agents=[fda_monitor_agent, cpt_monitor_agent, payer_monitor_agent, briefing_agent],
            tasks=[fda_task, cpt_task, payer_task, briefing_task],
            verbose=True,
        )
        briefing_html = crew.kickoff()

        save_briefing({
            "client_id": profile["client_id"],
            "week_of": week_of,
            "briefing": briefing_html if isinstance(briefing_html, str) else str(briefing_html),
        })

        notion_url = push_briefing_to_notion(
            client_id=profile["client_id"],
            founder_name=profile["founder_name"],
            briefing_text=briefing_html if isinstance(briefing_html, str) else str(briefing_html),
            week_of=week_of,
        )

        send_regulatory_briefing(
            recipient_email=profile["email"],
            founder_name=profile["founder_name"],
            briefing_html=briefing_html if isinstance(briefing_html, str) else str(briefing_html),
            week_of=week_of,
        )

        print(f"[RegulatoryAgent] Briefing complete for {profile['founder_name']} — Notion: {notion_url}")

    print("[RegulatoryAgent] Weekly pipeline run complete.")

if __name__ == "__main__":
    run_pipeline()
