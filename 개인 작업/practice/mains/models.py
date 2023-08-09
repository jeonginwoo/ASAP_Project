from django.db import models


class Menu(models.Model):
    image = models.ImageField(verbose_name='이미지',null = True, blank= True)
    name = models.CharField(max_length = 25, verbose_name='메뉴명')
    price = models.IntegerField(verbose_name='가격', default=10000)
    calorie = models.FloatField(verbose_name='칼로리', default=100.5)