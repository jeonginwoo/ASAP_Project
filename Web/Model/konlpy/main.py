#pip install konlpy 하시면 됩니다
#https://github.com/ssut/py-hanspell
#노션-ASAP프로젝트-GPT 안에 DataSet 아래에 kkma-2.0.zip 다운 받고 압축 해제하면 kkma-2.0.jar 나옴
#......\Lib\site-packages\konlpy\java 파일 들어가면 kkma-2.0.jar 있는데 압축 해제한거로 대체하면 단어 인식 훨씬 잘해줌
from hanspell import spell_checker
import re

def __init__():
    from konlpy.tag import Kkma
    global kkma
    kkma = Kkma()

# 바꿀 단어들을 사전 형태로 정의
replacements = {
    "알러지": "알레르기",
    "슈레드치즈": "슈레디드치즈",
    "모짜렐라치즈":"슈레디드치즈",
    "강판치즈":"슈레디드치즈",
    "마늘칩":"마늘",
    "열량":"칼로리",
    "헤ㄹ로디아블로와푸어":"헬로디아블로와퍼",
    "헤ㄹ로릴리트와푸어":"헬로릴리트와퍼",
    "헤ㄹ로이나리우스와푸어":"헬로이나리우스와퍼",
    "몬스터엑스":"몬스터X",
    "블랙바비큐와푸어":"블랙바비큐와퍼",
    "비프앤슈림프버거":"비프&슈림프버거",
    "하어쉬브라운":"해쉬브라운",
    "치즈스틱":"21치즈스틱",
    "얼니얼ㄴ링":"어니언링",
    "크리미모짜아보ㄹ":"크리미모짜볼",
    "코우리스ㄹ로":"코울슬로",
    "굽ㄴ갈릭시즈닝":"구운갈릭시즈닝",
    "스윗얼니얼ㄴ시즈닝":"스윗어니언시즈닝",
    "망고서ㄴ데":"망고선데",
    "초코망고서ㄴ데":"초코망고선데",
    "아이스아아메리카노":"아이스아메리카노",
    "순수":"순수(미네랄워터)",
    "하ㄹ라피뇨":"할라피뇨",
    "비엘티":"BLT",
    "비앨티":"BLT",
    "헤ㄹ로":"헬로",
    "와푸어":"와퍼",
    # 다른 단어들도 필요하다면 추가로 정의할 수 있습니다.
}

queryName = {'헬로디아블로와퍼':'헬로_디아블로_와퍼', '헬로릴리트와퍼':'헬로_릴리트_와퍼','헬로이나리우스와퍼':'헬로_이나리우스_와퍼',
            '구운갈릭시즈닝':'구운갈릭_시즈닝', '스윗어니언시즈닝':'스윗어니언_시즈닝','매콤치즈시즈닝':'매콤치즈_시즈닝',
            '망고선데':'망고_선데','초코망고선데':'초코_망고_선데','컵망고아이스크림':'컵_망고_아이스크림','코카콜라제로':'코카콜라_제로',
            '스프라이트제로':'스프라이트_제로','미닛메이드오렌지':'미닛메이드_오렌지','아이스아메리카노':'아이스_아메리카노'}

toQ = {'칼로리': 'N_calories','포화지방': 'N_saturated_fat','단백질': 'N_protein','당': 'N_sugars','설탕': 'N_sugars','나트륨': 'N_sodium','카페인':'N_caffeine',
       '우유알레르기': 'A_milk','치킨알레르기': 'A_Chicken','돼지고기알레르기': 'A_pork','돼지알레르기': 'A_pork','소고기알레르기': 'A_beef','소알레르기':'A_beef',
       '비프알레르기': 'A_beef','계란알레르기': 'A_egg','달걀알레르기': 'A_egg','오징어알레르기': 'A_squid','토마토알레르기': 'A_tomato',
       '조개알레르기': 'A_clam','새우알레르기': 'A_shrimp','갑각류알레르기': 'A_clam A_shrimp','치즈': 'I_sliced_cheese I_shredded_cheese','슬라이스치즈': 'I_sliced_cheese','슈레디드치즈': 'I_shredded_cheese',
       '피클': 'I_pickle','할라피뇨': 'I_jalapeno','통새우': 'I_whole_shrimp','베이컨': 'I_bacon','양상추': 'I_lettuce','양파': 'I_onion','해쉬브라운': 'I_hashbrown',
       '토마토': 'I_tomato','마늘': 'I_garlic_chip','마늘칩': 'I_garlic_chip','마요': 'S_mayo','마요네즈': 'S_mayo','마요네즈소스': 'S_mayo','불고기': 'S_bulgogi',
       '불고기소스': 'S_bulgogi','바베큐': 'S_barbecue','바베큐소스': 'S_barbecue','케찹': 'S_ketchup','케찹소스': 'S_ketchup','디아블로': 'S_diablo',
       '디아블로소스': 'S_diablo','매운토마토': 'S_spicy_tomato','매운토마토소스': 'S_spicy_tomato','매운': 'S_diablo S_spicy_tomato','치즈소스': 'S_cheese','타르타르': 'S_tartar',
       '타르타르소스': 'S_tartar','베이컨잼': 'S_baconjam','베이컨잼소스': 'S_baconjam','머스타드': 'S_mustard','머스타드소스': 'S_mustard',
       '소고기': 'P_beef P_steak','비프': 'P_beef','새우': 'P_shrimp','쉬림프': 'P_shrimp','슈림프': 'P_shrimp','치킨': 'P_chicken','닭': 'P_chicken','스테이크': 'P_steak',
      '알레르기':'a', '영양소':'n', '영양성분':'n', '가격':'price','정보':'info','상세정보':'info','맵기':'spicy',
      '햄버거':'M','버거':'M','아침':'M','점심':'M','저녁':'M','메뉴':'M','음식':'M','끼니':'M','배고프':'M','드시':'M','먹':'M',
       '사이드':'S','디저트':'DD','음료수':'DD','아이스크림':'DD','높':'desc','낮':'asc','많':'desc','적':'asc','차갑':'ice','차':'ice',
      '시원':'ice','따시':'hot','따듯':'hot','뜨겁':'hot'}

ham = ['와퍼','치즈와퍼','불고기와퍼','갈릭불고기와퍼','콰트로치즈와퍼','통새우와퍼','롱치킨버거',
        '와퍼주니어','치즈와퍼주니어','불고기와퍼주니어','콰트로치즈와퍼주니어','통새우와퍼주니어',
        '헬로디아블로와퍼','헬로이나리우스와퍼','헬로릴리트와퍼','치킨킹BLT','치킨킹','롱치킨','바비큐치킨버거',
        '치킨버거','슈림프버거','통새우슈림프버거','비프슈림프버거','블랙바비큐콰트로치즈와퍼','블랙바비큐와퍼',
        '비프불고기버거','비프앤슈림프버거','비프&슈림프버거','몬스터와퍼','몬스터X','더블비프불고기버거','더블오리지날치즈버거',
      '치킨와퍼','콰트로','주니어','롱치킨','헬로','이나리우스','릴리트','BLT','몬스터','더블비프','바비큐치킨','블랙']
side = ['너겟킹','치즈스틱','어니언링','바삭킹','쉐이킹프라이','크리미모짜볼','코코넛슈림프','21치즈스틱',
        '치즈프라이','프렌치프라이','코울슬로','콘샐러드','구운갈릭시즈닝','스윗어니언시즈닝','매콤치즈시즈닝']
drink = ['망고선데','초코망고선데','레드애플맛제로','레몬라임맛제로','컵망고아이스크림','아메리카노','아이스아메리카노','핫초코','아이스초코','코카콜라',
        '코카콜라제로','스프라이트','스프라이트제로','미닛메이드오렌지','순수','순수(미네랄워터)']
neu = ['칼로리','열량','포화지방','단백질','당','설탕','나트륨','카페인', 
       'N_calories','N_staurated_fat','N_protein','N_sugars','N_sodium','N_caffeine']
al = ['우유알레르기','치킨알레르기','돼지고기알레르기','돼지알레르기','소고기알레르기','소알레르기','비프알레르기','계란알레르기','달걀알레르기',
          '오징어알레르기','토마토알레르기','조개알레르기','새우알레르기','갑각류알레르기']
ing = ['치즈','슬라이스치즈','슈레디드치즈','피클','할라피뇨','통새우','베이컨','양상추','양파','해쉬브라운','토마토','마늘','마늘칩']
sau = ['마요','마요네즈','마요네즈소스','불고기','불고기소스','바베큐','바베큐소스','케찹','케찹소스','디아블로','디아블로소스',
      '매운토마토','매운토마토소스','치즈소스','타르타르','타르타르소스','베이컨잼','베이컨잼소스','머스타드','머스타드소스']
pat = ['소고기','비프','새우','쉬림프','슈림프','치킨','닭','스테이크']
etc = ['영양소','영양성분','알레르기','가격','정보','상세정보','맵기','맵','안맵','nutrition_info','allergy',
       'N','A','price','info','spicy','높','많','낮','적','차갑','차','시원','따시','따듯','뜨겁','ice','hot']
cat = ['M','S','DD','햄버거','버거','사이드','디저트','음료수','아이스크림','아침','점심','배고프','저녁','메뉴','음식','끼니','드시','먹']
eve = ham+side+drink+neu+al+ing+sau+pat+etc+cat

def replace_multiple_words(text):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text

def toQuery(a):
    a = replace_multiple_words(a)
    m = kkma.morphs(a) # 형태소 추출
    n = kkma.nouns(a) # 명사만 추출

    #print('원래 문장 : ' + a)



    mor = []
    ct = 0
    full = ''
    count=0
    what = 'M'

    for i in range(ct,len(m)):
        full+=m[i]
    while ct<len(m)-1:
        tmp = full
        for i in range(len(m)-1, ct-1, -1):
            if i==ct:
                mor.append(m[ct])
                full=full[len(m[ct]):]
                ct+=1
                break
            if tmp in replacements: tmp = replacements[tmp] 
            if tmp in eve:
                if tmp in side+['사이드'] : what = 'S'
                elif tmp in drink+['디저트','음료수','아이스크림'] : what = 'DD'
                mor.append(tmp)
                for j in range(ct, i+1) : full=full[len(m[j]):]
                ct = i+1
                break

            tmp=tmp[:len(tmp)-len(m[i])]
    if full!='' : mor.append(full)

    #print('mor')
    #print(mor)
        
        
        
    re1 = [] # 결과
    sg = ['추가','넣', '들어가', '좋', '들어가', '듣', '있'] # 주문 - 추가 키워드
    si = [] # 주문 - 들어가는 키워드
    sb = ['없', '빼주', '빼', '싫','안'] # 주문 - 빼는
    en = ['에', '에다', '에다가'] # 공백 키워드

    #주문 토큰화
    for i in mor: # 형태소로 나뉘었을 때
        if i in eve:
            re1.append(i)
        elif i in sg+sb: # 형태소 단위로 주문 키워드 넣기
            if i in sg:
                re1.append('1') # 들어가는거
            elif i in si:
                re1.append('i') # 정보
            elif i in sb:
                re1.append('0') # 빼는거
            #else : print('어라' + 'g') # 혹시 오류
    #print('re1')
    #print(re1) # 첫 결과


    #토큰 결합
    re2 = [] # 찐 결과 리스트
    tmp = '' # 임시로 이을 문장
    for i in re1: # 토큰
        if i in toQ.keys() : i = toQ[i]
        if i in en: # 공백 키워드가 들어오면 리스트에 넣고 tmp 초기화
            tmp = '1 ' + tmp
            re2.append(tmp)
            tmp = ''
        elif i in ['0','1']: # 주문 키워드 들어오면 tmp에 추가 후 리스트 넣고 tmp 초기화
            tmp = i + ' ' + tmp
            re2.append(tmp)
            tmp = ''
        elif tmp == '' : # tmp가 빈 배열일 때 무조건 더하기
            tmp+=(i + ' ')
        else : tmp += (i + ' ') # 그 이외 (명사)는 추가
    if tmp!='' : re2.append('1 ' + tmp)

    #print(re2)


    re3 = []
    for i in range(len(re2)):
        how = ''
        for j in re2[i].split():
            if j in neu+cat+['A','N','asc','desc']: 
                re3.append(j)
            elif j in ham+side+drink:
                if j in ham: what = 'M'
                elif j in side : what = 'S'
                elif j in drink : what = 'DD'
                if j in queryName: j = queryName[j]
                re3.append('menu_name ' + j)
            elif j in etc:
                if j == '맵': re3.append('spicy' + ' 1')
                elif j == '안맵': re3.append('spicy' + ' 0')
                elif j == 'ice' : re3.append('ishot' + ' 0')
                elif j == 'hot' : re3.append('ishot' + ' 1')
                else:
                    re3.append('_' + j)
            elif j in ['0','1'] : how = j
            else :
                re3.append(j + ' ' + how)

    return re3