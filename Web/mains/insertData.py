import os
import sys
import csv
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")

from mains.models import BurgerTable, SideTable, DDTable

def insert_Menu():
    with open('C:/Projects/ASAP_Project/Data/버거단품_CSV.csv', encoding = 'utf-8') as csv_file:
            data_reader = csv.reader(csv_file)
            next(data_reader,None)
            for row in data_reader:
                  if row[0]:
                    # 각 행의 데이터를 읽어서 모델 객체 생성 및 저장
                    for i in range(10,19):
                        if row[i] == 'True' or row[i] == 'TRUE':
                            row[i] = True
                        else:
                            row[i] = False
                    for i in range(30,40):
                        if row[i] == 'True' or row[i] == 'TRUE':
                            row[i] = True
                        else:
                            row[i] = False

                    menu = BurgerTable(
                        menu_name=row[0],
                        price=row[1],
                        image=row[2],
                        info=row[3],
                        spicy=row[4],
                        N_calories=row[5],
                        N_protein=row[6],
                        N_sodium=row[7],
                        N_sugars=row[8],
                        N_saturated_fat=row[9],
                        A_milk=row[10],
                        A_chicken=row[11],
                        A_pork=row[12],
                        A_beef=row[13],
                        A_egg=row[14],
                        A_squid=row[15],
                        A_tomato=row[16],
                        A_clam=row[17],
                        A_shrimp=row[18],
                        I_sliced_cheese=row[19],
                        I_shredded_cheese=row[20],
                        I_pickle=row[21],
                        I_jalapeno=row[22],
                        I_whole_shrimp=row[23],
                        I_bacon=row[24],
                        I_tomato=row[25],
                        I_lettuce=row[26],
                        I_onion=row[27],
                        I_hashbrown=row[28],
                        I_garlic_chip=row[29],
                        S_mayo=row[30],
                        S_bulgogi=row[31],
                        S_barbecue=row[32],
                        S_ketchup=row[33],
                        S_diablo=row[34],
                        S_spicy_tomato=row[35],
                        S_cheese=row[36],
                        S_tartar=row[37],
                        S_baconjam=row[38],
                        S_mustard=row[39],
                        P_beef=row[40],
                        P_shrimp=row[41],
                        P_chicken=row[42],
                        P_steak=row[43],
                        R_rank=row[44],
                        R_man=row[45],
                        R_women=row[46],
                        R_yman=row[47],
                        R_ywomen=row[48],
                        R_oman=row[49],
                        R_owomen=row[50],
                        R_young=row[51],
                        R_old=row[52],
                        R_summer=row[53],
                        R_winter=row[54],
                    )
                    menu.save()

def insert_Side():
    with open('/Users/ho/데청캠/D_Git/ASAP_Project/Data/사이드_CSV.csv') as csv_file:
            data_reader = csv.reader(csv_file)
            next(data_reader,None)
            for row in data_reader:
                  if row[0]:
                    # 각 행의 데이터를 읽어서 모델 객체 생성 및 저장
                    for i in range(11,20):
                        if row[i] == 'True' or row[i] == 'TRUE':
                              row[i] = True
                        else:
                             row[i] = False

                    menu = SideTable(
                        menu_name=row[0],
                        price=row[1],
                        image=row[2],
                        info=row[3],
                        rank=row[4],
                        spicy=row[5],
                        N_calories=row[6],
                        N_protein=row[7],
                        N_sodium=row[8],
                        N_sugars=row[9],
                        N_saturated_fat=row[10],
                        A_milk=row[11],
                        A_chicken=row[12],
                        A_pork=row[13],
                        A_beef=row[14],
                        A_egg=row[15],
                        A_squid=row[16],
                        A_tomato=row[17],
                        A_clam=row[18],
                        A_shrimp=row[19],
                    )
                    menu.save()

def insert_DD():
    with open('/Users/ho/데청캠/D_Git/ASAP_Project/Data/음료&디저트_CSV.csv') as csv_file:
            data_reader = csv.reader(csv_file)
            next(data_reader,None)
            for row in data_reader:
                  if row[0]:
                    # 각 행의 데이터를 읽어서 모델 객체 생성 및 저장
                    for i in range(12, 22):
                        if row[i] == 'True' or row[i] == 'TRUE':
                              row[i] = True
                        else:
                             row[i] = False

                    menu = DDTable(
                        menu_name=row[0],
                        price=row[1],
                        image=row[2],
                        info=row[3],
                        rank=row[4],
                        spicy=row[5],
                        N_calories=row[6],
                        N_protein=row[7],
                        N_sodium=row[8],
                        N_sugars=row[9],
                        N_saturated_fat=row[10],
                        N_caffeine=row[11],
                        A_milk=row[12],
                        A_chicken=row[13],
                        A_pork=row[14],
                        A_beef=row[15],
                        A_egg=row[16],
                        A_squid=row[17],
                        A_tomato=row[18],
                        A_clam=row[19],
                        A_shrimp=row[20],
                        A_peach=row[21],
                    )
                    menu.save()
