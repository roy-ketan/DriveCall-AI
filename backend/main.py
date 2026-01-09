from fastapi import FastAPI, WebSocket
from vad import is_speech
from stt import speech_to_text
from llm import generate_reply
from tts import text_to_speech

app = FastAPI()

@app.websocket("/call")
async def handle_call(ws: WebSocket):
    await ws.accept()

    while True:
        audio_chunk = await ws.receive_bytes()

        if is_speech(audio_chunk):
            text = await speech_to_text(audio_chunk)
            reply = await generate_reply(text)
            audio_reply = await text_to_speech(reply)

            await ws.send_bytes(audio_reply)
