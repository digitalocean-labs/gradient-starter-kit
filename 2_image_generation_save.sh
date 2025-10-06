#!/bin/bash
# Generate an image and save it directly as a PNG file.
# Uses jq to extract the Base64 data and pipes it to a file.

curl https://inference.do-ai.run/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -d '{
    "model": "openai-gpt-image-1",
    "prompt": "A cute baby sea otter floating on its back in calm blue water",
    "n": 1,
    "size": "1024x1024"
  }' | jq -r '.data[0].b64_json' | base64 --decode > sea_otter.png
