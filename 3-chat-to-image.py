from openai import OpenAI
import base64
from dotenv import load_dotenv
import os

load_dotenv()

# Client for DigitalOcean Inference
client = OpenAI(
    base_url="https://inference.do-ai.run/v1/",
    api_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY")
)

prompt = """
A whimsical illustration of a futuristic robot joyfully cooking pasta
in a cozy kitchen, with steam rising from the pot and a curious cat
watching from the floor.
"""

result = client.images.generate(
    model="openai-gpt-image-1",   # ✅ DO’s image model
    prompt=prompt,
    size="512x512",
    n=1                # DO often requires explicit size
)

# Save image to file
image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

with open("robot_pasta.png", "wb") as f:
    f.write(image_bytes)

print("Saved robot_pasta.png")
