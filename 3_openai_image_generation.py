# Generate an image and save it as a PNG file using the OpenAI SDK.
# Takes a text prompt and outputs an actual image file.

from openai import OpenAI
from dotenv import load_dotenv
import os, base64

load_dotenv()

client = OpenAI(
    base_url="https://inference.do-ai.run/v1/",
    api_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY"),
)

result = client.images.generate(
    model="openai-gpt-image-1",
    prompt="A cute baby sea otter, children's book drawing style",
    size="1024x1024",
    n=1
)

b64 = result.data[0].b64_json
with open("sea_otter.png", "wb") as f:
    f.write(base64.b64decode(b64))

print("Saved sea_otter.png")
