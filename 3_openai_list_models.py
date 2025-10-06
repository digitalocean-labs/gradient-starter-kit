# List all available models using the OpenAI SDK.
# Same as the curl version, but easier to use in Python code.

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://inference.do-ai.run/v1/",
    api_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY"),
)

models = client.models.list()
for m in models.data:
    print("-", m.id)
