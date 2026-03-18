import resend
from config.settings import settings

resend.api_key = settings.resend_api_key

def send_regulatory_briefing(recipient_email: str, founder_name: str, briefing_html: str, week_of: str):
    html_body = f"""
    <html><body style='font-family:sans-serif;max-width:700px;margin:auto'>
      <h2 style='color:#1a237e'>⚖️ Regulatory & Reimbursement Briefing</h2>
      <p style='color:#555'>Week of {week_of} — prepared for <strong>{founder_name}</strong> by The Faulkner Group</p>
      <hr/>
      {briefing_html}
      <hr/>
      <p style='font-size:12px;color:#999'>Powered by Regulatory Agent — The Faulkner Group Advisors</p>
    </body></html>
    """
    resend.Emails.send({
        "from": settings.briefing_from_email,
        "to": recipient_email,
        "subject": f"Your Regulatory Briefing — Week of {week_of}",
        "html": html_body,
    })
    print(f"Regulatory briefing sent to {recipient_email}")
