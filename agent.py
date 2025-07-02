from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import openai, cartesia, deepgram, noise_cancellation, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv()

class Assistant(Agent):
    def __init__(self):
        super().__init__(instructions="You are a helpful AI voice assistant.")

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt=deepgram.STT(model="nova-3", language="en"),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=cartesia.TTS(model="sonic-2"),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )
    await ctx.connect()
    await session.generate_reply(instructions="Hello! How can I help you today?")

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
