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
from django.db.models import QuerySet
from django.core.serializers import serialize
from .dictStorage import col_dict

import json

k = Ko_Bert()
nlp = Konlp()

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

def test(request):
    return render(request,'main/menuReco.html')



# 프론트에서 음성 인식으로 Request를 받았을 때 처리함
def speechRecognition(request):
    if request.method == 'POST':
        recordData = request.body

        # 이 부분에 추후 Wisper 모델 적용 및 DB 쿼리 작성 예정
        with open('../test_record_data.wav', 'wb') as mpeg:
            mpeg.write(recordData)
            # 위스퍼 실행
            transcription = transcriber("../test_record_data.wav")
            print(transcription)
            #text = transcription['text']
            text = '칼로리로 높은 걸로 추천해 줘'

            i_result = inputBert(text)
            result = inputKonlp(text)
            print(result)



            result = inputKonlp(text)
            final_result = menuReco(result)
            print(final_result)

            for i in range(len(result)):
                if result[i] =='or':
                    continue
                if i == 0 and len(result) == 1:
                    answer = '말씀하신'
                    answer = answer +' ' +"#" + col_dict[result[i]] +" #"+ col_dict[str(i_result)] +'등의 키워드로 추천한 메뉴 입니다.'
                elif i == 0:
                    answer = '말씀하신 '
                    answer = answer +' '+'#' + col_dict[result[i]]
                    
                elif i >0 and len(result) -1 > i:
                    answer = answer +' '+ '#'  + col_dict[result[i]]
                    
                elif len(result)-1 == i and i_result == 0:
                    answer = answer +'#' +col_dict[result[i]] + ' 등의 키워드로 '+col_dict[str(i_result)] + '한 메뉴 입니다.'
                else:
                    answer = answer +'#' +col_dict[result[i]]+'#'+col_dict[str(i_result)] + '등의 키워드로 추천한 메뉴 입니다.'
                    
            print(answer)
            # 제시하신 "노인","인기메뉴" 등의 키워드로 추천한 메뉴입니다.

            burger_list_json = serialize('json', final_result['burger_list'])
            side_list_json = serialize('json', final_result['side_list'])
            dd_list_json = serialize('json',  final_result['dd_list'])

            burger_list = json.loads(burger_list_json)
            side_list = json.loads(side_list_json)
            dd_list = json.loads(dd_list_json)

            context = {
            'speaker' : text,
            'burger_list': burger_list,
            'side_list' : side_list,
            'dd_list' : dd_list,
                        }
            
            # 추천해야하는 메뉴가 없는 경우
            if len(burger_list_json) == 2 and len(side_list_json) == 2 and len(dd_list_json) == 2:
                context = {
                    'speaker' : text,
                    'error' : '죄송합니다. 말씀하신 내용과 관련된 추천 가능한 메뉴가 없습니다.',
                }
                return JsonResponse(context)
        #if len(burger_list) == 0 and len(side_list) == 0 and len(dd_list) == 0:
            #response_data = {'message': 'Audio data received and processed successfully'}
            # return render(request, 'main/menuReco.html',context)

            return JsonResponse(context)

    # Request의 method가 POST 방식이 아닌 GET 방식임
    #return JsonResponse({'message': 'This request is GET method', "status": 405}, status = 405)
    #return render(request, 'main/menuReco.html')

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

def menuReco(keyword):
    burger_list = []
    side_list = []
    dd_list = []
    b_query = Q()
    s_query = Q()
    dd_query = Q()

    # query_list = ['menu_name 제로', 'DnD']
    # query_list = ['menu_name 치즈']
    # query_list = ['menu_name 아이스_아메리카노']
    # query_list = ['I_tomato 1']
    # query_list = ['menu_name 너겟킹']

    query_list = keyword


    if not query_list: # 들어온 값이 없으면 인기메뉴 추천
        query_list = ['rank 1']

    if  query_list[-1] not in ['M', 'S', 'DD','asc','desc']: # 구분 없는 질문이면 else로 분류
        query_list.append('else')



    #print("----쿼리 생성 부분----")
    # __contains : 해당 문자열이 포함되어 있는 것들 출력
    # __lte : ... 이하인 것들 출력 (lt는 미만)
    # __gte : ... 이상인 것들 출력 (gt는 초과)
    orCount = 0
    for query in query_list[:-1]:   # ['or', 'cheese1 1', 'cheese2 1', 'else']
        if query == 'or':
            tempQuery = query
            orCount = 3
            continue
        if orCount != 0:
            tempQuery += " " + query
            orCount -= 1
            if orCount!=1:
                continue
            orCount -= 1
            query = tempQuery

        # print("------------------")
        # print(f'query : {query}')
        # print("------------------")

        # ['or cheese1 1 cheese2 1']
        tlist = query.split()
        # ['or', 'cheese1', '1', 'cheese2', '2']
        if len(tlist) == 1:
            tlist.append('1')
        if tlist[0] != 'or':
            tlist[1] = tlist[1].replace('_', ' ')

        # print()
        # print("------------------")
        # print("tlist : ", tlist)
        # print("------------------")
        # print()

        if tlist[0] == 'or':
            b_query &= Q(**{tlist[1]:tlist[2]}) | Q(**{tlist[3]:tlist[4]})
            burger_list = BurgerTable.objects.filter(b_query).order_by('rank')[:4]

        elif query_list[-1] == 'M':  # 버거 질문
            b_query &= Q(**{tlist[0]+'__contains':tlist[1]})
            burger_list = BurgerTable.objects.filter(b_query).order_by('rank')[:4]

        elif query_list[-1] == 'S':  # 사이드 질문

            s_query &= Q(**{tlist[0]+'__contains':tlist[1]})
            side_list = SideTable.objects.filter(s_query).order_by('rank')[:4]

        elif query_list[-1] == 'DD':   # 음료&디저트 질문
            dd_query &= Q(**{tlist[0]+'__contains':tlist[1]})
            dd_list = DDTable.objects.filter(dd_query).order_by('rank')[:4]
        elif query_list[-1] == 'asc':   # 칼로리 낮은순으로
            burger_list = BurgerTable.objects.all().order_by(f'{tlist[0]}')[:4]

        elif query_list[-1] == 'desc':   # 칼로리 높은 순으로
            burger_list = BurgerTable.objects.all().order_by(f'-{tlist[0]}')[:4]


        else:   # 기타 질문
            if tlist[0] == 'rank':
                b_query &= Q(**{tlist[0]+'__lte':3})
                burger_list = BurgerTable.objects.filter(b_query).order_by(tlist[0])#.values(*['menu_name', 'price', 'image', 'rank', 'I_sliced_cheese', 'I_shredded_cheese','I_pickle','I_jalapeno','I_whole_shrimp','I_bacon','I_lettuce','I_onion','I_hashbrown','I_tomato','I_garlic_chip'])
            elif tlist[0] == 'N_calories':
                b_query &= Q(**{tlist[0]:tlist[1]})
                burger_list = BurgerTable.objects.filter(b_query).order_by(tlist[0])#.values(*['menu_name', 'price', 'image', 'rank', 'N_calories', 'N_protein','N_sodium','N_sugars','N_saturated_fat'])[:3]
            else:
                try:
                    print(tlist)
                    b_query &= Q(**{tlist[0]+'__contains':tlist[1]})
                    burger_list = BurgerTable.objects.filter(b_query).order_by('rank')[:4]
                except:
                    burger_list = QuerySet()
                try:
                    s_query &= Q(**{tlist[0]+'__contains':tlist[1]})
                    side_list = SideTable.objects.filter(s_query).order_by('rank')[:4]
                except:
                    side_list = QuerySet()
                try:
                    dd_query &= Q(**{tlist[0]+'__contains':tlist[1]})
                    dd_list = DDTable.objects.filter(dd_query).order_by('rank')[:4]
                except:
                    dd_list = QuerySet()

    # print("----쿼리 생성----")
    # print("burger_list : ", burger_list)
    # print("side_list : ", side_list)
    # print("dd_list : ", dd_list)

    context = {'burger_list':burger_list, 'side_list':side_list, 'dd_list':dd_list}
    
    #render(request, 'main/menuReco.html', context)
    return context


def inputBert(text_file):
    result = k.start(text_file)
    print(result)
    return result

def inputKonlp(text_file):
    nlp_result = nlp.toQuery(text_file)
    if nlp_result:
        print(nlp_result)
    return nlp_result

