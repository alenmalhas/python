#Note: The openai-python library support for Azure OpenAI is in preview.
import os
from openai import OpenAI


client = OpenAI(base_url="http://xps15:1234/v1", api_key="not-needed")
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate",
    },
    {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
 ]

response = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages = messages,
  temperature=0,
  max_tokens=350,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

output_model = response.choices[0].message.content
output_formatted = output_model.replace('\\n', '\n').replace('\\t', '\t')

print(output_formatted)