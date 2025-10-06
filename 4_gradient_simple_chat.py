# Simple chat using DigitalOcean's native Gradient SDK.
# Works just like the OpenAI version, but designed specifically for DigitalOcean.

from gradient import Gradient
from dotenv import load_dotenv
import os

load_dotenv()

client = Gradient(model_access_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY"))

resp = client.chat.completions.create(
    model="llama3-8b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a fun fact about octopuses."}
    ],
)

print(resp.choices[0].message.content)
