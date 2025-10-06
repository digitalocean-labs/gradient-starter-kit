# Chat with an agent using the OpenAI SDK.
# The agent has access to your uploaded docs and knowledge base.

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://agents.do-ai.run/v1/",
    api_key=os.getenv("DIGITAL_OCEAN_AGENT_ACCESS_KEY"),
)

response = client.chat.completions.create(
    model="llama3-8b-instruct",
    messages=[
        {"role": "user", "content": "Summarize the pricing details mentioned in the uploaded docs."}
    ],
)

print(response.choices[0].message.content)
