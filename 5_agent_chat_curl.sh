#!/bin/bash
# Chat with a Gradient agent that has access to your knowledge base.
# Replace AGENT_ENDPOINT and AGENT_ACCESS_KEY with your actual values.

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
