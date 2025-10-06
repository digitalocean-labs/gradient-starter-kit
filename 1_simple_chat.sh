#!/bin/bash
# Send a simple chat message to llama3-8b-instruct.
# Your first "hello world" test to make sure chat completions work.

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
