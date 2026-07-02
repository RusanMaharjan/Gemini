import os
from google import genai

client = genai.Client(api_key = os.getenv('GEMINI_API_KEY'))

def gemini(text):
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input = text
    )
    return interaction.output_text