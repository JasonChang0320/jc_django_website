from django.shortcuts import render
from django.http import JsonResponse
import json
import os

# Create your views here.
def showtemplate(request):
    return render(request, 'index.html')

def show_google_map(request):
    return render(request,"map.html")

def grid_dataset(request):
    with open("statics/map.geojson") as f:
        data=json.load(f)

    return JsonResponse(data)

