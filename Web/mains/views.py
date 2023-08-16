from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MenuTable
from .serializers import MenuSerializer
from django.http import JsonResponse
from config.settings import transcriber
import json

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

# 결제 페이지 이동
def purchase(request):
    return render(request, 'main/purchase.html')

# 프론트에서 음성 인식으로 Request를 받았을 때 처리함
def speechRecognition(request):
    if request.method == 'POST':
        recordData = request.body

        # 이 부분에 추후 Wisper 모델 적용 및 DB 쿼리 작성 예정
        with open('../test_record_data.wav', 'wb') as mpeg:
            mpeg.write(recordData)

        transcription = transcriber('C:/Users/joung/Visual_Studio_Code_Workspace/repos/ASAP_Project/test_record_data.wav')

        data = {"message": transcription}

        return JsonResponse(data)

    # Request의 method가 POST 방식이 아닌 GET 방식임
    return JsonResponse({'message': 'This request is GET method', "status": 405}, status = 405)

# 프론트에서 텍스트로 Request를 받았을 때 처리함
def textInput(request):
    if request.method == 'POST':
        try:
            text_data = request.body
            text_data = json.loads(text_data)

            # 이 부분에 추후 모델 적용 및 DB 쿼리 작성

            data = {"message": text_data['value']}

            return JsonResponse(data)
        except: # Requset 형식이 올바른 JSON 형식이 아님
            return JsonResponse({"message": "Invalid JSON format!", "status": 400}, status = 400)

    # Request의 method가 POST 방식이 아닌 GET 방식임
    return JsonResponse({'message': 'This request is GET method', "status": 405}, status = 405)

def testTable(request):
    menu_list = MenuTable.objects.all()
    context = {'menu_list': menu_list}
    return render(request, 'main/menu_list.html', context)
