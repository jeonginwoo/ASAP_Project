from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def purchase(request):
    return render(request, 'main/purchase.html')