from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pipelines.weekly_regulatory_run import run_pipeline
from config.settings import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RegulatoryAgentScheduler")

scheduler = BlockingScheduler()
scheduler.add_job(
    func=run_pipeline,
    trigger=IntervalTrigger(days=settings.run_cadence_days),
    id="weekly_regulatory_pipeline",
    name="Weekly Women's Health Regulatory Pipeline",
    replace_existing=True,
)

if __name__ == "__main__":
    logger.info(f"Regulatory Agent Scheduler starting — every {settings.run_cadence_days} days.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler stopped.")
