import numpy as np
from silero_vad import load_silero_vad, get_speech_timestamps

model = load_silero_vad()

def is_speech(audio_chunk, sample_rate=16000):
    audio = np.frombuffer(audio_chunk, dtype=np.int16).astype("float32")
    timestamps = get_speech_timestamps(audio, model, sampling_rate=sample_rate)
    return len(timestamps) > 0
