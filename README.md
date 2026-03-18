# ⚖️ Regulatory Agent — FDA, CPT & Payer Intelligence

An agentic AI system built for **The Faulkner Group** advisory clients — women's health tech founders who need continuous monitoring of FDA clearance paths, CPT code changes, payer policy updates, and prior authorization trends.

This agent runs weekly and delivers structured regulatory briefings per founder profile so no one is blindsided at the growth stage.

---

## 🎯 Purpose

Reimbursement pathways are the single biggest barrier to scaling women's health tech. This agent ensures founders always know:
- Their FDA pathway status and recent precedents
- Which CPT codes apply and if they're changing
- What major payers (UHC, Aetna, BCBS, CMS) are covering or denying
- Prior auth trends and medical policy updates affecting their product category

---

## 📦 Monitoring Scope

| Domain | Sources |
|---|---|
| FDA Clearances | FDA 510(k) database, De Novo, PMA, FDA news |
| CPT Code Updates | AMA CPT, CMS NCCI edits |
| Payer Policies | CMS LCD/NCD, UHC, Aetna, BCBS medical policies |
| Prior Auth Trends | Perplexity research + payer portal monitoring |
| Regulatory Guidance | FDA guidance documents, Federal Register |
| State Mandates | State insurance mandates for women's health |

---

## 🏗 Architecture

```
regulatory-agent/
├── agents/
│   ├── fda_monitor_agent.py       # Tracks FDA clearances + guidance
│   ├── cpt_monitor_agent.py       # Monitors CPT code changes
│   ├── payer_monitor_agent.py     # Tracks payer policy + prior auth
│   └── briefing_agent.py          # Synthesizes weekly founder briefing
├── tools/
│   ├── fda_tool.py                # FDA open.fda.gov API
│   ├── cms_tool.py                # CMS LCD/NCD API
│   ├── perplexity_tool.py         # Payer + CPT web research
│   └── federal_register_tool.py   # Federal Register API
├── pipelines/
│   └── weekly_regulatory_run.py   # Full orchestration pipeline
├── db/
│   └── supabase_client.py
├── delivery/
│   ├── email_briefing.py          # Weekly regulatory briefing email
│   └── notion_push.py             # Notion regulatory tracker
├── profiles/
│   └── founder_profiles.py        # Founder product + regulatory context
├── scheduler/
│   └── cron_runner.py
├── config/
│   └── settings.py
├── .github/
│   └── workflows/
│       ├── regulatory-pipeline.yml
│       └── manual-test-run.yml
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🚀 Setup

```bash
git clone https://github.com/jsfaulkner86/regulatory-agent
cd regulatory-agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python pipelines/weekly_regulatory_run.py
```

---

*Built by The Faulkner Group — Agentic AI for Women's Health Founders*
