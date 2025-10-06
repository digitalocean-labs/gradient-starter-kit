from openai import OpenAI
import base64
from dotenv import load_dotenv
import os

load_dotenv()

# DigitalOcean Inference client
client = OpenAI(
    base_url="https://inference.do-ai.run/v1/",
    api_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY"),
)

prompt = "A cute baby sea otter, children’s book drawing style"

# Generate image via DO API
result = client.images.generate(
    model="openai-gpt-image-1",   # ✅ DO’s image model
    prompt=prompt,
    size="1024x1024",
    n=1
)

# Decode base64 into PNG
image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

with open("sea_otter.png", "wb") as f:
    f.write(image_bytes)

print("Saved sea_otter.png")
