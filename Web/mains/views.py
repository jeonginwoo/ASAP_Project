from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MenuTable, SideTable, DDTable
from .serializers import MenuSerializer
from django.http import JsonResponse
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
        with open('../test_record_data.mp3', 'wb') as mpeg:
            mpeg.write(recordData)

        data = {"message": "Response OK!"}

        return JsonResponse(data)

    # Request의 method가 POST 방식이 아닌 GET 방식임
    return JsonResponse({"message": "This request is GET method"})

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

def testBurger(request):
    print(request)
    burger_list = MenuTable.objects.all()
    context = {'burger_list': burger_list}
    return render(request, 'main/burger_list.html', context)

def testSide(request):
    print(request)
    side_list = SideTable.objects.all()
    context = {'side_list': side_list}
    return render(request, 'main/side_list.html', context)

def testDD(request):
    print(request)
    dd_list = DDTable.objects.all()
    context = {'dd_list': dd_list}
    return render(request, 'main/dd_list.html', context)

def menuQuery(request):
    a = ['0 S_bulgogi', '1 I_sliced_cheese', '1 I_shredded_cheese']
    d = {}

    if 'M_menu_list' in d:
        menu_list = MenuTable.objects.get(M_menu_list=d['M_menu_list'])
        context = {'menu_list':menu_list}
        return render(request, 'main/testRecommend.html', context)
    elif 'S_menu_list' in d:
        side_list = SideTable.objects.get(S_menu_list=d['S_menu_list'])
        context = {'side_list':side_list}
        return render(request, 'main/testRecommend.html', context)
    elif 'DD_menu_list' in d:
        DD_list = DDTable.objects.get(DD_menu_list=d['DD_menu_list'])
        context = {'DD_list':DD_list}
        return render(request, 'main/testRecommend.html', context)
    else:
        menu_list = MenuTable.objects.all()
        side_list = SideTable.objects.all()
        DD_list = DDTable.objects.all()
        context = {'menu_list':DD_list, 'side_list':side_list, 'DD_list':DD_list}
        return render(request, 'main/testRecommend.html', context)
