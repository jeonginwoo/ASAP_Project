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
                    for i in range(11,20):
                        if row[i] == 'True' or row[i] == 'TRUE':
                            row[i] = True
                        else:
                            row[i] = False
                    for i in range(31,41):
                        if row[i] == 'True' or row[i] == 'TRUE':
                            row[i] = True
                        else:
                            row[i] = False

                    menu = BurgerTable(
                        M_menu_name=row[0],
                        M_price=row[1],
                        M_image=row[2],
                        M_info=row[3],
                        M_rank=row[4],
                        M_spicy=row[5],
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
                        I_sliced_cheese=row[20],
                        I_shredded_cheese=row[21],
                        I_pickle=row[22],
                        I_jalapeno=row[23],
                        I_whole_shrimp=row[24],
                        I_bacon=row[25],
                        I_tomato=row[26],
                        I_lettuce=row[27],
                        I_onion=row[28],
                        I_hashbrown=row[29],
                        I_garlic_chip=row[30],
                        S_mayo=row[31],
                        S_bulgogi=row[32],
                        S_barbecue=row[33],
                        S_ketchup=row[34],
                        S_diablo=row[35],
                        S_spicy_tomato=row[36],
                        S_cheese=row[37],
                        S_tartar=row[38],
                        S_baconjam=row[39],
                        S_mustard=row[40],
                        P_beef=row[41],
                        P_shrimp=row[42],
                        P_chicken=row[43],
                        P_steak=row[44],
                    )
                    menu.save()

def insert_Side():
    with open('C:/Projects/ASAP_Project/Data/사이드_CSV.csv', encoding = 'utf-8') as csv_file:
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
                        S_menu_name=row[0],
                        S_price=row[1],
                        S_image=row[2],
                        S_info=row[3],
                        S_rank=row[4],
                        S_spicy=row[5],
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
    with open('C:/Projects/ASAP_Project/Data/음료&디저트_CSV.csv', encoding = 'utf-8') as csv_file:
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
                        DD_menu_name=row[0],
                        DD_price=row[1],
                        DD_image=row[2],
                        DD_info=row[3],
                        DD_rank=row[4],
                        DD_spicy=row[5],
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