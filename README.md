🔐 Step 1: Clone & Navigate to Project Directory

   git clone < https://github.com/VIGNESWARAN552/Call_Agent_LiveKit >

📦 Step 2: Install Project Dependencies

   pip install -r requirements.txt

🔐 Step 3: Configure Your Environment
Create a .env file at the root of your project directory and populate it with your credentials:

LIVEKIT_API_KEY=<livekit_api_key>
LIVEKIT_API_SECRET=<livekit_api_secret>
LIVEKIT_HOST=https://<livekit_host_url>

OPENAI_API_KEY=<openai_api_key>
DEEPGRAM_API_KEY=<deepgram_api_key>
CARTESIA_API_KEY=<cartesia_api_key>
TWILIO_SIP_TRUNK_SID=<twilio_sip_trunk_sid>

🎙️ Step 4: Launch the Voice AI Agent
Interactive Console Mode (recommended for testing/debugging):

  python agent.py console

Production Mode (ready for live phone interactions):

  python agent.py start

📞 Step 5: Making an Outbound Call
Execute the outbound call script:

   python outbound_call.py









