from deepgram import Deepgram
from config import DEEPGRAM_API_KEY

dg = Deepgram(DEEPGRAM_API_KEY)

async def speech_to_text(audio_bytes):
    response = await dg.transcription.prerecorded(
        {"buffer": audio_bytes, "mimetype": "audio/wav"},
        {"punctuate": True, "language": "en"}
    )
    return response["results"]["channels"][0]["alternatives"][0]["transcript"]
