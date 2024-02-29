# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://xps15:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

output_model = completion.choices[0].message.content
output_formatted = output_model.replace('\\n', '\n').replace('\\t', '\t')
#print(f'{output_model}')
print(output_formatted)