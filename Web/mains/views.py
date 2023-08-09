from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Menu
from .serializers import MenuSerializer


def index(request):
    return render(request, 'main/index.html')


class MenuDetailView(APIView):
    def get(self,request,menu_key):
        try:
            menu = Menu.objects.get(name=menu_key)
            serializer = MenuSerializer(menu)
            return Response(serializer.data)
        except Menu.DoesNotExist:
            return Response({"error" : "Menu not found"}, status= 404)
        

