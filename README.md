# DigitalOcean Gradient AI - Quick Reference Guide

If you're looking to get started with [DigitalOcean Gradient](https://docs.digitalocean.com/products/gradient-ai-agentic-cloud/) and want to quickly start building, this is a collection of examples, code snippets, and guides to help you hit the ground running.

Gradient gives you **serverless inference** — one API key that lets you use models from **OpenAI, Anthropic, DeepSeek, Llama, Qwen**, and others — all from a single endpoint.

---

## What You Can Do with Gradient

**DigitalOcean Gradient** provides two core AI platform offerings:

1. **Inference** —  
   Run models like GPT-4, Llama 3, DeepSeek, and others directly via a unified API endpoint.  
   Ideal for quick text, image, and embedding tasks.

2. **Agents** —  
   Create persistent, context-aware agents connected to your own data — docs, URLs, buckets, or files.  
   These agents “remember” what you’ve uploaded and respond with that context built in.

---

## Three Ways to Use Gradient

You can interact with either **Inference** or **Agents** in any of these ways:

| Method | Description | Example Section |
|--------|--------------|----------------|
| **cURL / REST API** | Use raw HTTP requests — fastest way to test and explore the API. | [Section 0 → List Models](#0-getting-started-serverless-inference) / [Section 1 → Simple Chat](#1-simple-chat-completion) |
| **OpenAI SDK** | Use the official OpenAI client and simply override the `base_url`. Fully compatible with the OpenAI API spec. | [Section 3 → Using Python (OpenAI SDK)](#3-using-python-openai-sdk) |
| **Gradient SDK** | Use DigitalOcean’s native Python client (`gradient`) — includes both Inference and Agents. | [Section 4 → Using Python (Gradient SDK)](#4-using-python-gradient-sdk) |

> All three methods are API-compatible — you can switch between them with minimal code changes.

---

## Quick Start Summary

Here’s a quick map of what you can do and where to find it in this guide:

| Goal | Endpoint | Example Section | SDK Equivalent |
|------|-----------|-----------------|----------------|
| 🔍 **List available models** | `GET /v1/models` | [0. Getting Started](#0-getting-started-serverless-inference) | `client.models.list()` |
| 💬 **Chat completion (text)** | `POST /v1/chat/completions` | [1. Simple Chat Completion](#1-simple-chat-completion) | `client.chat.completions.create()` |
| 🖼️ **Image generation** | `POST /v1/images/generations` | [2. Image Generation](#2-image-generation) | `client.images.generate()` |
| 🧠 **Query your own data (Agents)** | `POST /api/v1/chat/completions` *(agent-specific endpoint)* | [5. Agents and Knowledge Bases](#5-agents-and-knowledge-bases) | `Gradient(agent_access_key=...).chat.completions.create()` |
| ⚙️ **List agent models** | `GET /api/v1/models` *(agent-specific endpoint)* | [5. Agents and Knowledge Bases](#5-agents-and-knowledge-bases) | `client.models.list()` |

> 💡 You can switch seamlessly between **cURL**, the **OpenAI SDK**, or the **Gradient SDK** — all follow the same pattern and JSON structure.

---

## 📘 Using this Kit

This repo contains everything you need to start building with DigitalOcean Gradient AI:

* **This README** — complete guide with explanations and examples  
* **Standalone code files** — all curl commands (`.sh`) and Python scripts (`.py`) extracted and numbered by section (e.g., `0_list_models.sh`, `3_openai_simple_chat.py`)  
* **Jupyter notebook** — an interactive version of this guide (`playground.ipynb`) you can run in VS Code, Jupyter, or Google Colab  

Pick whichever format works best for you — read the guide, run the scripts directly, or work through the notebook interactively.

---

## 0. Getting Started (Serverless Inference)

If you just want to call models directly — no setup, no GPUs, no servers — this is where you start.

Gradient’s **serverless inference** lets you send prompts to models from OpenAI, Anthropic, DeepSeek, Llama, and more using a **single API key**.

You’ll need a **Model Access Key**, which you can create from your DigitalOcean account.

Once you have it, try this quick check to make sure it’s working:

```python
%%bash
curl -X GET https://inference.do-ai.run/v1/models \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -H "Content-Type: application/json"
```

> If everything’s set up correctly, you’ll get a list of available models back — things like `llama3-8b-instruct`, `gpt-4o-mini`, and `openai-gpt-image-1`.
> That’s your confirmation that the key works and you’re ready to start making requests.

---

## 1. Simple Chat Completion

Start with something small to make sure your setup works.
This one uses **llama3-8b-instruct**, a great general-purpose model.

```python
%%bash
curl https://inference.do-ai.run/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -d '{
    "model": "llama3-8b-instruct",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Tell me a fun fact about octopuses."}
    ]
  }'
```

> You should get back a short text response from the model.
> That’s your “it works” moment. 🎉

---

## 2. Image Generation

Once chat works, you can try generating an image.
Same API key, just a different model and endpoint.

```python
%%bash
curl https://inference.do-ai.run/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -d '{
    "model": "openai-gpt-image-1",
    "prompt": "A cute baby sea otter floating on its back in calm blue water",
    "n": 1,
    "size": "1024x1024"
  }'
```

> That will return JSON with a Base64 image string.

If you want to save it as a file, just pipe it through `jq` and `base64`:

```python
%%bash
curl https://inference.do-ai.run/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -d '{
    "model": "openai-gpt-image-1",
    "prompt": "A cute baby sea otter floating on its back in calm blue water",
    "n": 1,
    "size": "1024x1024"
  }' | jq -r '.data[0].b64_json' | base64 --decode > sea_otter.png
```

> After a few seconds, you should have a file called **sea_otter.png** sitting in your folder.

---

## 3. Multimodal Models (Fal)

Gradient now supports **multimodal models** from **Fal**, available through **Serverless Inference**.
You can use these to generate **images** and **audio** using the same API pattern you’ve already used for text and image tasks.

---

### Available Models

| Type      | Model ID                                | Description                                                                 |
| --------- | --------------------------------------- | --------------------------------------------------------------------------- |
| 🖼️ Image | `fal-ai/fast-sdxl`                      | Stable Diffusion XL (fast) — high-quality, high-resolution image generation |
| 🖼️ Image | `fal-ai/flux/schnell`                   | FLUX.1 (schnell) — fast image generation for prototyping                    |
| 🔊 Audio  | `fal-ai/stable-audio-25/text-to-audio`  | Stable Audio — convert text to natural-sounding audio                       |
| 🔊 Audio  | `fal-ai/elevenlabs/tts/multilingual-v2` | ElevenLabs Multilingual v2 — text-to-speech with multilingual support       |

These models use the same **inference endpoint**:

```
https://inference.do-ai.run
```

> To use these models, opt in to the [Fal Models Public Preview](https://cloud.digitalocean.com/account/feature-preview?feature=fal-models) in the DigitalOcean console.
> Access is typically available within 10–15 minutes after opting in.

---

### Example 1: Generate an Image (Fal FLUX.1 Schnell)

```python
%%bash
curl -sS -X POST 'https://inference.do-ai.run/v1/async-invoke' \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": "fal-ai/flux/schnell",
    "input": { "prompt": "A high-quality photo of a futuristic city at sunset" }
  }'
```

This starts an asynchronous job and returns a `request_id`.

---

### Check Job Status

Use the request ID to check progress:

```python
%%bash

curl -sS -X GET "https://inference.do-ai.run/v1/async-invoke/$REQUEST_ID/status" \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY"
```


Keep polling this endpoint until you see:

```json
{ "status": "COMPLETE" }
```

---

### Retrieve the Result

Once the job completes, fetch the final output (includes the image URL):

```python
%%bash

curl -sS -X GET "https://inference.do-ai.run/v1/async-invoke/$REQUEST_ID" \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY"
```


The response contains a URL to the generated file.

---
### Example 2: Generate an Image with Customized Parameters

```python
%%bash
curl -sS -X POST 'https://inference.do-ai.run/v1/async-invoke' \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": "fal-ai/fast-sdxl",
    "input": {
      "prompt": "A high-quality photo of a futuristic city at sunset",
      "output_format": "landscape_4_3",
      "num_inference_steps": 4,
      "guidance_scale": 3.5,
      "num_images": 1,
      "enable_safety_checker": true
    },
    "tags": [
      { "key": "type", "value": "test" }
    ]
  }'
```

---

### Example 3: Generate Sound (Text → Audio)

```python
%%bash

curl -sS -X POST 'https://inference.do-ai.run/v1/async-invoke' \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": "fal-ai/stable-audio-25/text-to-audio",
    "input": {
      "prompt": "Futuristic epic song",
      "seconds_total": 60
    },
    "tags": [
      { "key": "type", "value": "test" }
    ]
  }'
```
---
### Example 4: Generate Audio (Fal ElevenLabs Multilingual TTS)

```python
%%bash
curl -sS -X POST 'https://inference.do-ai.run/v1/async-invoke' \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": "fal-ai/elevenlabs/tts/multilingual-v2",
    "input": {
      "text": "Welcome to Gradient — generating audio from text.",
      "voice": "Rachel",
      "language": "en"
    }
  }'
```

This returns a `request_id`, which you can use to check status and retrieve the final audio file.

---

### Summary

| Action           | Endpoint                                   | Example                           |
| ---------------- | ------------------------------------------ | --------------------------------- |
| Start async job  | `POST /v1/async-invoke`                    | Submit prompt or input            |
| Check status     | `GET /v1/async-invoke/{request_id}/status` | Wait until `"status": "COMPLETE"` |
| Get final result | `GET /v1/async-invoke/{request_id}`        | Fetch generated file              |

> These async endpoints work for both **image** and **audio** generation tasks.

---

## 3. Using Python (OpenAI SDK)

Once the cURL tests work, it's easier to move to Python.
You can use either the **OpenAI SDK** (just point it at the DigitalOcean endpoint) or the **Gradient SDK** (DigitalOcean's native one).

---

### OpenAI SDK (pointed at DigitalOcean Inference)

#### List models

```python
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
```

#### Simple chat

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://inference.do-ai.run/v1/",
    api_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY"),
)

resp = client.chat.completions.create(
    model="llama3-8b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a fun fact about octopuses."}
    ],
)

print(resp.choices[0].message.content)
```

#### Image generation

```python
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
    prompt="A cute baby sea otter, children’s book drawing style",
    size="1024x1024",
    n=1
)

b64 = result.data[0].b64_json
with open("sea_otter.png", "wb") as f:
    f.write(base64.b64decode(b64))

print("Saved sea_otter.png")
```

---

## 4. Using Python (Gradient SDK)

### Gradient SDK (native DigitalOcean client)

If you prefer to use DigitalOcean's native SDK, the setup is almost the same — just a slightly different client.

#### List available models

```python
from gradient import Gradient
from dotenv import load_dotenv
import os

load_dotenv()

client = Gradient(model_access_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY"))

models = client.models.list()

print("Available models:")
for model in models.data:
    print(f"  - {model.id}")
```

#### Simple chat

```python
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
```

#### Image generation

```python
from gradient import Gradient
from dotenv import load_dotenv
import os, base64

load_dotenv()

client = Gradient(model_access_key=os.getenv("DIGITAL_OCEAN_MODEL_ACCESS_KEY"))

result = client.images.generations.create(
    model="openai-gpt-image-1",
    prompt="A cute baby sea otter, children’s book drawing style",
    size="1024x1024",
    n=1
)

b64 = result.data[0].b64_json
with open("sea_otter.png", "wb") as f:
    f.write(base64.b64decode(b64))

print("Saved sea_otter.png")
```

---

## Handy Differences (at a glance)

* **Auth variable**: `DIGITAL_OCEAN_MODEL_ACCESS_KEY`
* **OpenAI SDK** → add `base_url="https://inference.do-ai.run/v1/"`
* **Gradient SDK** → use `model_access_key`, no base URL needed
* **Image model name** → `openai-gpt-image-1` (DigitalOcean’s version)
* Always include `n` and `size` when generating images

---

## 5. Agents and Knowledge Bases

Agents are like custom versions of a model that “know” your stuff.

They sit on top of your uploaded knowledge — docs, PDFs, URLs, or connected data sources — and respond with that context built in. Think of them as “your model + your knowledge base” that lives on DigitalOcean.

You don’t have to manage a database or index anything yourself. Gradient handles all of it.

---

### How it works (conceptually)

1. **Create a Knowledge Base**
   You can:

   * Upload files manually (PDFs, docs, text files)
   * Point to a public URL
   * Connect a **DigitalOcean Spaces** or **S3 bucket**
   * Even link to a **Dropbox folder**

2. **Create an Agent**
   Once you have a knowledge base, you connect it to an agent.
   The agent is what you’ll actually talk to — it uses your chosen model (e.g., Llama, GPT-4, etc.) and the knowledge base behind the scenes.

3. **Get your Agent Endpoint & Access Key**
   Gradient gives you two things:

   * An **endpoint URL** for that specific agent
   * An **access key** (different from your model access key)

You can then query that agent using **cURL**, the **OpenAI SDK**, or the **Gradient SDK** — same pattern as before, just with the agent endpoint.

---

### Example 1: Chat with an Agent (cURL)

Replace `AGENT_ENDPOINT` and `AGENT_ACCESS_KEY` with the values from your Gradient dashboard.

```python
%%bash
curl -i \
  -X POST "$AGENT_ENDPOINT/api/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AGENT_ACCESS_KEY" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "How do I make this coffee stronger?"
      }
    ],
    "stream": false,
    "include_functions_info": false,
    "include_retrieval_info": false,
    "include_guardrails_info": false
  }'

```

> If everything’s configured correctly, your agent will respond using the knowledge base you connected to it.

---

### Example 2: Chat with an Agent (OpenAI SDK)

```python
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
```

---

### Example 3: Chat with an Agent (Gradient SDK)

```python
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
```

> Notice how the code looks almost identical to the inference examples — just a different key and base URL.

---

### Quick Notes

* **Inference** → uses `https://inference.do-ai.run/v1/`
* **Agents** → uses `https://agents.do-ai.run/v1/`
* You’ll have separate keys for both (`MODEL_ACCESS_KEY` and `AGENT_ACCESS_KEY`)
* Both APIs follow the **OpenAI API spec**, so you can use the same SDK for both
* The **Gradient SDK** wraps both inference and agent APIs under one interface

---

### Typical Use Case

* Use **Inference** for quick, on-demand tasks (chat, image, embeddings, etc.)
* Use **Agents** when you want a persistent model that “remembers” or “knows” something — like your documentation, internal policies, or dataset.

---

Once you've got your agent working, you can integrate it anywhere — a chatbot UI, an internal Slack bot, a product support tool, or even your own API layer.

---

## Using the Jupyter Notebook

This repo includes a **playground.ipynb** file — an interactive notebook version of this guide.

### Setting up your API keys

Before running the notebook, you'll need to set up your API keys:

**For local use (VS Code, Jupyter):**

1. Copy the `.env-example` file to `.env`:
   ```bash
   cp .env-example .env
   ```

2. Edit `.env` and add your actual API keys:
   - `DIGITAL_OCEAN_MODEL_ACCESS_KEY` — for serverless inference
   - `AGENT_ENDPOINT` — your agent's endpoint URL
   - `AGENT_ACCESS_KEY` — for agent access

**For Google Colab:**

Add your keys to the **Secrets** section in Colab (the 🔑 icon in the sidebar) using these names:
- `DIGITAL_OCEAN_MODEL_ACCESS_KEY`
- `AGENT_ENDPOINT`
- `AGENT_ACCESS_KEY`

---

You can use the notebook in a few different ways:

### Option 1: VS Code (Jupyter Extension)

If you're using VS Code, just open `playground.ipynb` and the Jupyter extension will let you run the code cells directly.

### Option 2: Jupyter Notebook or JupyterLab

If you have Jupyter installed locally, run:

```bash
jupyter notebook playground.ipynb
```

or

```bash
jupyter lab playground.ipynb
```

### Option 3: Google Colab

You can also upload `playground.ipynb` to [Google Colab](https://colab.research.google.com/) and run it there — no local setup required.

---

### Regenerating the Notebook

If you make changes to this **README.md** file and want to update the notebook, you can use the **jupytext** tool:

```bash
pip install jupytext
jupytext --to notebook README.md -o playground.ipynb
```

This will regenerate `playground.ipynb` from the markdown file, keeping everything in sync.