# Generate an image using the Gradient SDK.
# DigitalOcean's native way to create images from text prompts.

from gradient import Gradient
from dotenv import load_dotenv
import os, base64

load_dotenv()

client = Gradient(model_access_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY"))

result = client.images.generations.create(
    model="openai-gpt-image-1",
    prompt="A cute baby sea otter, children's book drawing style",
    size="1024x1024",
    n=1
)

b64 = result.data[0].b64_json
with open("sea_otter.png", "wb") as f:
    f.write(base64.b64decode(b64))

print("Saved sea_otter.png")
