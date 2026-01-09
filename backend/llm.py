import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def generate_reply(user_text):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an automotive call center AI."},
            {"role": "user", "content": user_text}
        ]
    )
    return response.choices[0].message.content
