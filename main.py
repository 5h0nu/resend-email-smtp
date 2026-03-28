import os
import httpx
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Simple Mailer")

# 1. Configuration (Set your API Key here)
RESEND_API_KEY = os.getenv("RESEND_API_KEY", "resendapi_key")
FROM_EMAIL = "support@sh0nu.in"

# 2. Simplified Data Model
class EmailRequest(BaseModel):
    to: List[str]
    subject: str
    message: str

@app.post("/send-email")
async def send_email(req: EmailRequest):
    # Resend Free Tier usually limits to batching 50 emails at once via BCC
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "from": f"SHANU <{FROM_EMAIL}>",
                "to": [FROM_EMAIL], # Sent 'to' you to prevent 'To' field clutter
                "bcc": req.to,      # Real recipients go here
                "subject": req.subject,
                "html": f"<p>{req.message}</p>"
            }
        )
        
        if res.status_code not in [200, 201]:
            raise HTTPException(status_code=res.status_code, detail=res.text)
            
        return {"status": "success", "resend_id": res.json().get("id")}

@app.get("/")
async def root():
    return {"message": "API is Online. Go to /docs to send emails."}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
