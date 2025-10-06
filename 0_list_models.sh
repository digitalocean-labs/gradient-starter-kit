#!/bin/bash
# Quick check to see what models are available on DigitalOcean Gradient.
# This confirms your API key works and shows you all the models you can use.

curl -X GET https://inference.do-ai.run/v1/models \
  -H "Authorization: Bearer $DIGITAL_OCEAN_MODEL_ACCESS_KEY" \
  -H "Content-Type: application/json"
