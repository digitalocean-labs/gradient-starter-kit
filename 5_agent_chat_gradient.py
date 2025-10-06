# Chat with an agent using the Gradient SDK.
# Your agent can answer questions based on the documents you've uploaded.

from gradient import Gradient
from dotenv import load_dotenv
import os

load_dotenv()

client = Gradient(agent_access_key=os.getenv("DIGITAL_OCEAN_AGENT_ACCESS_KEY"))

response = client.chat.completions.create(
    model="llama3-8b-instruct",
    messages=[
        {"role": "user", "content": "Summarize the pricing details mentioned in the uploaded docs."}
    ],
)

print(response.choices[0].message.content)
