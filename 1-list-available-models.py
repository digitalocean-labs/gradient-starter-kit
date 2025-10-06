## Example 1: List Available Models
## This lists all available models from DigitalOcean Inference. Same code you’d use with OpenAI—you’re just pointing it at a DigitalOcean endpoint (base_url).

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://inference.do-ai.run/v1/",  # DO's Inference endpoint
    api_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY")
)

# List all available models
try:
    models = client.models.list()
    print("Available models:")
    for model in models.data:
        print(f"- {model.id}")
except Exception as e:
    print(f"Error listing models: {e}")