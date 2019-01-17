from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .Params import Params

# Create your views here.

@csrf_exempt
def index(request):
	
	if request.method == 'POST':
			body_unicode = request.body.decode('utf-8')
			data = json.loads(body_unicode)
			
			data_params = data["params"]
			params = {}
			for param in data_params:
				params[param["name"]] = param["value"]
			
			#print(params["CODI_ESTA"])
			return HttpResponse("POST, world. You're at the polls index.")
	elif request.method == 'GET':
    	    return HttpResponse("GET, world. You're at the polls index.")