import requests
import os

model_id =  os.getenv('EMBEDDING_MODEL')#"sentence-transformers/all-MiniLM-L6-v2"
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
hf_token = os.getenv('HF_ACCESS_TOKEN')
headers = {"Authorization": f"Bearer {hf_token}"}

def queryModel(input_text_array):
    response = requests.post(api_url, headers=headers, json={"inputs": input_text_array, "options":{"wait_for_model":True}})
    return response.json()