import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def call_llm(messages, temperature=0.2):
    prompt = "\n".join(
        f"{m['role'].upper()}: {m['content']}"
        for m in messages
    )

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    return response.text
