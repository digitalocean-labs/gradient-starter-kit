## Example 2: Run a Simple Chat Completion
## We’re using the same .chat.completions.create() method. Only the base_url is different.

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://inference.do-ai.run/v1/",  # DO's Inference endpoint
    api_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY")
)

# Run a simple chat completion
try:
    response = client.chat.completions.create(
        model="llama3-8b-instruct",  # Swap in any supported model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a fun fact about octopuses."}
        ]
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error during completion: {e}")