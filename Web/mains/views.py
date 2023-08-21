from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BurgerTable, SideTable, DDTable
#from .serializers import MenuSerializer
from django.http import JsonResponse
from django.db.models import Q
from config.settings import transcriber
from Model.Ko_Bert.main import *
from Model.Ko_Bert.CustomBertModel import *
from Model.Ko_Bert.CustomPredictor import *
from Model.konlpy.main import *
import json



def index(request):
    # 첫화면에 보여질 메뉴 설정중
    menu_list = BurgerTable.objects.all().values('menu_name','price','image').order_by('rank')[:6]
    context = {'menu_list': menu_list}
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

def menuReco(request):
    burger_list = []
    side_list = []
    dd_list = []
    b_query = Q()
    s_query = Q()
    dd_query = Q()

    query_list = ['menu_name 너겟킹', 'Side']
    query_list = ['menu_name 제로', 'DnD']
    query_list = ['menu_name 치즈']
    query_list = ['A_milk 1']

    if not len(query_list): # 들어온 값이 없으면 인기메뉴 추천
        query_list = ['rank 1']
    if query_list[-1] not in ['Burger', 'Side', 'DnD']: # 구분 없는 질문이면 else로 분류
                                                        # 승재가 구분해서 보내주면 좋을듯?
        query_list.append('else')

    # __contains : 해당 문자열이 포함되어 있는 것들 출력
    # __lte : ... 이하인 것들 출력 (lt는 미만)
    # __gte : ... 이상인 것들 출력 (gt는 초과)
    for query in query_list[:-1]:
        tlist = query.split()
        if len(tlist) == 1:
            tlist.append('1')
        tlist[1] = tlist[1].replace('_', ' ')

        if query_list[-1] == 'Burger':  # 버거 질문
            b_query &= Q(**{tlist[0]+'__contains':tlist[1]})
            burger_list = BurgerTable.objects.filter(b_query)
        
        elif query_list[-1] == 'Side':  # 사이드 질문
            s_query &= Q(**{tlist[0]+'__contains':tlist[1]})
            side_list = SideTable.objects.filter(s_query)

        elif query_list[-1] == 'DnD':   # 음료&디저트 질문
            dd_query &= Q(**{tlist[0]+'__contains':tlist[1]})
            dd_list = DDTable.objects.filter(dd_query)

        else:   # 기타 질문
            if tlist[0] == 'rank':
                if tlist[1]:
                    b_query &= Q(**{tlist[0]+'__lte':3})
                    burger_list = BurgerTable.objects.filter(b_query).order_by('rank').values(*['menu_name', 'price', 'image', 'rank', 'I_sliced_cheese', 'I_shredded_cheese','I_pickle','I_jalapeno','I_whole_shrimp','I_bacon','I_lettuce','I_onion','I_hashbrown','I_tomato','I_garlic_chip'])
            else:
                b_query &= Q(**{tlist[0]+'__contains':tlist[1]})
                s_query &= Q(**{tlist[0]+'__contains':tlist[1]})
                dd_query &= Q(**{tlist[0]+'__contains':tlist[1]})
                burger_list = BurgerTable.objects.filter(b_query)
                side_list = SideTable.objects.filter(s_query)
                dd_list = DDTable.objects.filter(dd_query)

    context = {'burger_list':burger_list, 'side_list':side_list, 'dd_list':dd_list}

    return render(request, 'main/testQuery.html', context)

def inputBert(text_file):
    k = Ko_Bert()
    result = k.start(text_file)
    print(result)
    return result

def inputKonlp(text_file):
    nlp_result = toQuery(text_file)
    print(nlp_result)
    return nlp_result

def bootstrap(request):
    burger_list = []
    side_list = []
    dd_list = []
    b_query = Q()
    s_query = Q()
    dd_query = Q()

    query_list = ['menu_name 너겟킹', 'Side']
    query_list = ['menu_name 제로', 'DnD']
    query_list = ['menu_name 치즈']
    query_list = ['menu_name 치즈', 'Burger']
    query_list = []

    if not len(query_list): # 들어온 값이 없으면 인기메뉴 추천
        query_list = ['rank 1']
    if query_list[-1] not in ['Burger', 'Side', 'DnD']: # 구분 없는 질문이면 else로 분류
        query_list.append('else')

    # __contains : 해당 문자열이 포함되어 있는 것들 출력
    # __lte : ... 이하인 것들 출력 (lt는 미만)
    # __gte : ... 이상인 것들 출력 (gt는 초과)
    for query in query_list[:-1]:
        tlist = query.split()
        if len(tlist) == 1:
            tlist.append('1')
        tlist[1] = tlist[1].replace('_', ' ')

        if query_list[-1] == 'Burger':  # 버거 질문
            b_query &= Q(**{tlist[0]+'__contains':tlist[1]})
            burger_list = BurgerTable.objects.filter(b_query)
            
        elif query_list[-1] == 'Side':  # 사이드 질문
            s_query &= Q(**{tlist[0]+'__contains':tlist[1]})
            side_list = SideTable.objects.filter(s_query)

        elif query_list[-1] == 'DnD':   # 음료&디저트 질문
            dd_query &= Q(**{tlist[0]+'__contains':tlist[1]})
            dd_list = DDTable.objects.filter(dd_query)

        else:   # 기타 질문
            if tlist[0] == 'rank':
                if tlist[1]:
                    b_query &= Q(**{tlist[0]+'__lte':3})
                    burger_list = BurgerTable.objects.filter(b_query).order_by('rank')
                else:
                    b_query &= Q(**{tlist[0]+'__gte':3})
                    burger_list = BurgerTable.objects.filter(b_query).order_by('-rank')
            else:
                b_query &= Q(**{tlist[0]+'__contains':tlist[1]})
                s_query &= Q(**{tlist[0]+'__contains':tlist[1]})
                dd_query &= Q(**{tlist[0]+'__contains':tlist[1]})
                burger_list = BurgerTable.objects.filter(b_query)
                side_list = SideTable.objects.filter(s_query)
                dd_list = DDTable.objects.filter(dd_query)

    context = {'burger_list':burger_list, 'side_list':side_list, 'dd_list':dd_list}
    
    return render(request, 'main/bootstrap.html', context)