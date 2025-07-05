import os
import asyncio
from dotenv import load_dotenv
from livekit import api

load_dotenv()

class TelephonyManager:
    def __init__(self):
        self.lkapi = api.LiveKitAPI()
        self.outbound_trunk_id = os.getenv("SIP_OUTBOUND_TRUNK_ID")

    async def make_call(self, phone_number):
        room_name = f"call-{phone_number.replace('+', '')}-{int(asyncio.get_event_loop().time())}"
        agent_name = "agent"  # ✅ using default agent name

        try:
            dispatch = await self.lkapi.agent_dispatch.create_dispatch(
                api.CreateAgentDispatchRequest(
                    agent_name=agent_name,
                    room=room_name,
                    metadata=phone_number
                )
            )
            print(f"✅ Agent dispatched to room: {room_name}")

            if not self.outbound_trunk_id or not self.outbound_trunk_id.startswith("ST_"):
                print("❌ SIP_OUTBOUND_TRUNK_ID is invalid")
                return

            sip_participant = await self.lkapi.sip.create_sip_participant(
                api.CreateSIPParticipantRequest(
                    room_name=room_name,
                    sip_trunk_id=self.outbound_trunk_id,
                    sip_call_to=phone_number,
                    participant_identity="phone_user"  # ✅ must match RoomInputOptions
                )
            )
            print(f"✅ SIP participant created. Call triggered to: {phone_number}")

        except Exception as e:
            print(f"❌ Error during SIP call: {e}")
        finally:
            await self.lkapi.aclose()

async def make_outbound_call():
    telephony = TelephonyManager()
    await telephony.make_call("+919345828403")  # your number here

if __name__ == "__main__":
    asyncio.run(make_outbound_call())
