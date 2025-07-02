import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = os.environ["TWILIO_PHONE_NUMBER"]
TO_PHONE_NUMBER = os.environ["TO_PHONE_NUMBER"]
SIP_USERNAME = os.environ["SIP_USERNAME"]
SIP_DOMAIN = os.environ["SIP_DOMAIN"]

# Debug print to check for spaces/errors
print("TWILIO_PHONE_NUMBER:", repr(TWILIO_PHONE_NUMBER))
print("TO_PHONE_NUMBER:", repr(TO_PHONE_NUMBER))

sip_uri = f"sip:{SIP_USERNAME}@{SIP_DOMAIN}"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

call = client.calls.create(
    to=TO_PHONE_NUMBER,
    from_=TWILIO_PHONE_NUMBER,
    twiml=f"""
<Response>
  <Dial>
    <Sip>{sip_uri}</Sip>
  </Dial>
</Response>
"""
)
print(f"Calling {TO_PHONE_NUMBER}, connected to {sip_uri}. Call SID: {call.sid}")
