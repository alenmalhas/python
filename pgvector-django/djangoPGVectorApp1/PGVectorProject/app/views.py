from django.shortcuts import render
from django.http import HttpResponse
from app.helpers import config, connect, model_helper

# Create your views here.
def index(request):
	dbConfig = config.db_config()
	return HttpResponse(f'index method executed, dbConfig: {dbConfig}')

def indexTwo(request):
	dbConfig = config.db_config()
	return HttpResponse(f'indexTwo method executed.')


def test1search(request):
	return HttpResponse('test1search method executed.')