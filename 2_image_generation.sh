#!/bin/bash
# Generate an image from a text prompt.
# Returns Base64-encoded JSON that you can decode into an actual image.

curl https://inference.do-ai.run/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -d '{
    "model": "openai-gpt-image-1",
    "prompt": "A cute baby sea otter floating on its back in calm blue water",
    "n": 1,
    "size": "1024x1024"
  }'
