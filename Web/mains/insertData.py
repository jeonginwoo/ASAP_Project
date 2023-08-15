import csv
from django.core.exceptions import ValidationError
from mains.models import MenuTable

def import_csv_to_database(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        
        for row in csv_reader:
            # 각 행의 데이터를 읽어서 모델 객체 생성 및 저장
            menu = MenuTable(
                menu_name=row['menu_name'],
                price=row['price'],
                image=row['image'],
                info=row['info'],
                rank=row['rank'],
                spicy=row['spicy'],
                N_calories=row['N_calories'],
                N_protein=row['N_protein'],
                N_sodium=row['N_sodium'],
                N_sugars=row['N_sugars'],
                N_saturated_fat=row['N_saturated_fat'],
                A_milk=row['A_milk'] == 'TRUE',
                A_Chicken=row['A_chicken'] == 'TRUE',
                Apork=row['Apork'] == 'TRUE',
                A_beef=row['A_beef'] == 'TRUE',
                A_egg=row['A_egg'] == 'TRUE',
                A_squid=row['A_squid'] == 'TRUE',
                A_tomato=row['A_tomato'] == 'TRUE',
                A_clam=row['A_clam'] == 'TRUE',
                A_shrimp=row['A_shrimp'] == 'TRUE',
                I_sliced_cheese=row['I_sliced_cheese'],
                I_shredded_cheese=row['I_shredded_cheese'],
                I_pickle=row['I_pickle'],
                I_jalapeno=row['I_jalapeno'],
                I_whole_shrimp=row['I_whole_shrimp'],
                I_bacon=row['I_bacon'],
                I_tomato=row['I_tomato'],
                I_lettuce=row['I_lettuce'],
                I_onion=row['I_onion'],
                I_hashbrown=row['I_hashbrown'],
                I_garlic_chip=row['I_garlic_chip'],
                S_mayo=row['S_mayo'] == 'TRUE',
                S_bulgogi=row['S_bulgogi'] == 'TRUE',
                S_barbecue=row['S_barbecue'] == 'TRUE',
                S_ketchup=row['S_ketchup'] == 'TRUE',
                S_diablo=row['S_diablo'] == 'TRUE',
                S_spicy_tomato=row['S_spicy_tomato'] == 'TRUE',
                S_cheese=row['S_cheese'] == 'TRUE',
                S_tartar=row['S_tartar'] == 'TRUE',
                S_baconjam=row['S_baconjam'] == 'TRUE',
                S_mustard=row['S_mustard'] == 'TRUE',
                P_beef=row['P_beef'],
                P_shrimp=row['P_shrimp'],
                P_chicken=row['P_chicken'],
                P_steak=row['P_steak'],
            )
            menu.save()
