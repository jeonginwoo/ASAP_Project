from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BurgerTable, SideTable, DDTable
#from .serializers import MenuSerializer
from django.http import JsonResponse
from config.settings import transcriber
from Model.Ko_Bert.main import *
from Model.Ko_Bert.CustomBertModel import *
from Model.Ko_Bert.CustomPredictor import *
from Model.konlpy.main import *
from django.db.models import Q,F
import json



def index(request):
    # 첫화면에 보여질 메뉴 설정중
    menu_list = BurgerTable.objects.all().values('menu_name','price','image').order_by('rank')[:6]
    side_list = SideTable.objects.all().values('menu_name','price','image').order_by('rank')[:6]
    drink_list = DDTable.objects.all().values('menu_name','price','image').order_by('rank')[:6]

    context = {
        'menu_list': menu_list,
        'side_list': side_list,
        'drink_list': drink_list,
               }

    return render(request, 'main/index.html',context)

# class MenuDetailView(APIView):
#     def get(self,request,menu_key):
#         try:
#             menu = Menu.objects.get(name=menu_key)
#             serializer = MenuSerializer(menu)
#             return Response(serializer.data)
#         except Menu.DoesNotExist:
#             return Response({"error" : "Menu not found"}, status= 404)

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
            transcription = transcriber("../test_record_data.mp3")
            print(transcription)
        inputBert(transcription['text'])
        inputKonlp(transcription['text'])


        data = {"message": "Response OK!"}

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

def testBurger(request):
    print(request)
    burger_list = BurgerTable.objects.all()
    context = {'burger_list': burger_list}
    return render(request, 'main/list/burger_list.html', context)

def testSide(request):
    print(request)
    side_list = SideTable.objects.all()
    context = {'side_list': side_list}
    return render(request, 'main/list/side_list.html', context)

def testDD(request):
    print(request)
    dd_list = DDTable.objects.all()
    context = {'dd_list': dd_list}
    return render(request, 'main/list/dd_list.html', context)

def testQuery(request):
    d = {}
    a = ['S_menu_name 너겟킹', 'I_sliced_cheese 1', 'I_shredded_cheese 1']

    for i in a:
        j = i.split()
        if len(j) == 1:
            j.append('0')
        j[1] = j[1].replace('_', ' ')
        d[j[0]] = j[1]

#     # SideTable.objects.filter(menu_name__startswith='너겟킹') # 너겟킹으로 시작하는 메뉴 찾기.
#     # BurgerTable.objects.filter(spicy__gt=0) # 맵기가 0보다 큰 메뉴 찾기

    query_string = ''

    # 특정 메뉴 찾기
    if 'M_menu_name' in d:
        menu_list = BurgerTable.objects.filter(menu_name__startswith=d['M_menu_name'])
        context = {'menu_list':menu_list}
        return render(request, 'main/testQuery.html', context)
    elif 'S_menu_name' in d:
        menu_list = SideTable.objects.filter(menu_name__startswith=d['S_menu_name'])
        context = {'menu_list':menu_list}
        return render(request, 'main/testQuery.html', context)
    elif 'DD_menu_name' in d:
        menu_list = DDTable.objects.filter(menu_name__startswith=d['DD_menu_name'])
        context = {'menu_list':menu_list}
        return render(request, 'main/testQuery.html', context)

    # 특정 메뉴가 아닌 경우 추천
    else:
        attribute, menu = ''
        for q in d.keys():
            if q == 'N':    # 햄버거가 특정 되었을 때
                attribute = 'N_calories, N_protein, N_sodium, N_sugars, N_saturated_fat'
            elif q == 'A':    # 햄버거가 특정 되었을 때
                query_string += ""


        query_string = f"SELECT {attribute} FROM BurgerTable WHERE {menu}"
        menu_list = BurgerTable.objects.raw(query_string)
        context = {'menu_list':menu_list}
        return render(request, 'main/testQuery.html', context)

def inputBert(text_file):
    k = Ko_Bert()
    result = k.start(text_file)
    print(result)
    return result

def inputKonlp(text_file):
    nlp_result = toQuery('케찹 들어가고 불고기 안들어간 햄버거 알려줘')
    if nlp_result:
        print(nlp_result)
        recommendMenu(nlp_result)
    return nlp_result

def recommendMenu(menu_list):
    # Django에서 동적으로 필드 이름을 사용하기 위해서는 Q 를 이용한다.
    key_list = []
    value_list = []
    for index in menu_list:
        word_list = index.split()
        if len(word_list) > 1 :
            value_list.append(word_list[0])
            key_list.append(word_list[1])

    filters = Q()

    for field_name, value in zip(key_list,value_list):
        filters &= Q(**{field_name: value})

    menu_list = BurgerTable.objects.filter(filters)
    print(menu_list)
    #추천메뉴는 최대 4개까지만 보여줄기위함
    if len(menu_list) > 4:
        pass

    # side_list = SideTable.objects.all().values('menu_name','price','image').order_by('rank')[:6]
    # drink_list = DDTable.objects.all().values('menu_name','price','image').order_by('rank')[:6]
