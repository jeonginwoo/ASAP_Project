from django.shortcuts import render
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'main/index.html')

def purchase(request):
    return render(request, 'main/purchase.html')

def speechRecognition(request):
    if request.method == 'POST':
        recordData = request.body

        with open('../test_record_data.mp3', 'wb') as mpeg:
            mpeg.write(recordData)

        data = {"message": "Response OK!"}

        return JsonResponse(data)
    
    return JsonResponse({"message": "This request is GET method"})
        