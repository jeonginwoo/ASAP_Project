import django
import csv

django.setup()

from .models import MenuTable

f = open('C:/Users/jiw41/Downloads/MenuTable', 'r', encoding='cp949')
info_list = []

rdr = csv.reader(f)
next(rdr)

for row in rdr:
    meue_name,price,image,info,rank,spicy,calories,protein,sodium,sugars,saturated_fat,Amilk,AChicken,Apork,Abeef,Aegg,Asquid,Atomato,Aclam,Ashrimp,sliced_cheese,shredded_cheese,pickle,jalapeno,whole_shrimp,bacon,tomato,lettuce,onion,hashbrown,garlic_chip,mayo,bulgogi,barbecue,ketchup,diablo,spicy_tomato,cheese,tartar,baconjam,mustard,Pbeef,Pshrimp,Pchicken,Psteak = row

    tuple = (meue_name,price,image,info,rank,spicy,calories,protein,sodium,sugars,saturated_fat,Amilk,AChicken,Apork,Abeef,Aegg,Asquid,Atomato,Aclam,Ashrimp,sliced_cheese,shredded_cheese,pickle,jalapeno,whole_shrimp,bacon,tomato,lettuce,onion,hashbrown,garlic_chip,mayo,bulgogi,barbecue,ketchup,diablo,spicy_tomato,cheese,tartar,baconjam,mustard,Pbeef,Pshrimp,Pchicken,Psteak)
    info_list.append(tuple)

f.close()

instances = []

for (meue_name,price,image,info,rank,spicy,calories,protein,sodium,sugars,saturated_fat,Amilk,AChicken,Apork,Abeef,Aegg,Asquid,Atomato,Aclam,Ashrimp,sliced_cheese,shredded_cheese,pickle,jalapeno,whole_shrimp,bacon,tomato,lettuce,onion,hashbrown,garlic_chip,mayo,bulgogi,barbecue,ketchup,diablo,spicy_tomato,cheese,tartar,baconjam,mustard,Pbeef,Pshrimp,Pchicken,Psteak) in info_list:
    instances.append(MenuTable(meue_name=meue_name, price=price, image=image, info=info, rank=rank, spicy=spicy, calories=calories, protein=protein, sodium=sodium, sugars=sugars, saturated_fat=saturated_fat, Amilk=Amilk, AChicken=AChicken, Apork=Apork, Abeef=Abeef, Aegg=Aegg, Asquid=Asquid, Atomato=Atomato, Aclam=Aclam, Ashrimp=Ashrimp, sliced_cheese=sliced_cheese, shredded_cheese=shredded_cheese, pickle=pickle, jalapeno=jalapeno, whole_shrimp=whole_shrimp, bacon=bacon, tomato=tomato, lettuce=lettuce, onion=onion, hashbrown=hashbrown, garlic_chip=garlic_chip, mayo=mayo, bulgogi=bulgogi, barbecue=barbecue, ketchup=ketchup, diablo=diablo, spicy_tomato=spicy_tomato, cheese=cheese, tartar=tartar, baconjam=baconjam, mustard=mustard, Pbeef=Pbeef, Pshrimp=Pshrimp, Pchicken=Pchicken , Psteak=Psteak))

print(instances)

MenuTable.objects.bulk_create(instances)