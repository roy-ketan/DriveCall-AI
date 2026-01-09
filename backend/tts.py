from deepgram import Deepgram
from config import DEEPGRAM_API_KEY

dg = Deepgram(DEEPGRAM_API_KEY)

async def text_to_speech(text):
    audio = await dg.speak.async_synthesize(text, {
        "voice": "aura-asteria-en",
        "encoding": "linear16",
        "sample_rate": 16000
    })
    return audio
