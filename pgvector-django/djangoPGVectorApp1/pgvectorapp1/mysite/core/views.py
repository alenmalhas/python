from django.shortcuts import render
from core.models import LangchainPgEmbedding
from pgvector.django import L2Distance

# Create your views here.
def index(request):
    if request.method == "POST":
        input_text = request.POST.get('input_text')
        input_embedding = QueryModelWithTextChunks(input_text)
        most_similar_doc = LangchainPgEmbedding.objects.order_by(
            L2Distance('embedding', input_embedding)
        ).first()
        context = {
            'input_text': input_text,
            'most_similar' : most_similar_doc
        }
        return render(request, 'index.html', context)
    
    embeddings = LangchainPgEmbedding.objects.all()
    doc = embeddings.first().document
    t1 =doc.title()
    context = {'embeddings':embeddings}
    return render(request, 'index.html', context)


import requests
import os

model_id = "sentence-transformers/all-MiniLM-L6-v2"
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
hf_token = os.getenv('HF_ACCESS_TOKEN')
headers = {"Authorization": f"Bearer {hf_token}"}

def QueryModelWithTextChunks(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()