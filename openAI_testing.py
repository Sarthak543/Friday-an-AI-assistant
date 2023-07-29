import os
import openai
from config import apiKey
openai.api_key = apiKey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="tell me about elephants.",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)


'''
{
  "id": "cmpl-7gYEcaeFkHh54GuSMtUSXnniIsxDY",
  "object": "text_completion",
  "created": 1690375730,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nElephants are the largest terrestrial animals on Earth. They are found in parts of Africa and Asia. Elephants have a unique set of physical features, including a long trunk, large ears, and two long tusks which are used for protection and digging. They also have four-toenails on each foot and each species has a distinct set of wrinkles and skin markings. Elephants live in large family groups of about 12 and have complex social structures. They are primarily herbivores, but also scavenge for meat when it is available. Elephants are considered keystone species, meaning they are a critical part of their habitat and affect the environment as a whole. They have been shown to have strong emotional bonds, advanced communication skills, and collaborate to solve complex problems.",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 5,
    "completion_tokens": 162,
    "total_tokens": 167
  }
}
'''