# Simple chat completion using the OpenAI SDK.
# Point the OpenAI client at DigitalOcean's endpoint and it just works.

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://inference.do-ai.run/v1/",
    api_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY"),
)

resp = client.chat.completions.create(
    model="llama3-8b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a fun fact about octopuses."}
    ],
)

print(resp.choices[0].message.content)
