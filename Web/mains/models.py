from django.db import models


class Menu(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    name = models.CharField(max_length=25, verbose_name='메뉴명')
    price = models.IntegerField(verbose_name='가격', default=10000)
    calorie = models.FloatField(verbose_name='칼로리', default=100.5)

class TestMenuTable(models.Model):
    name = models.CharField(max_length=25, verbose_name='메뉴명')
    price = models.IntegerField(default=5000, verbose_name='가격')    # integer? float? char?
    image = models.ImageField(null=True, blank=True, verbose_name='이미지')
    #ingredients = models.IntegerField(verbose_name='재료')
    info = models.TextField(verbose_name='정보')

    ### 재료
    Bulgogi = models.BooleanField(default=False, verbose_name='불고기')
    Chicken = models.BooleanField(default=False, verbose_name='치킨')
    Shrimp = models.BooleanField(default=False, verbose_name='새우')
    Beef = models.BooleanField(default=False, verbose_name='소고기')
    Bacon = models.BooleanField(default=False, verbose_name='베이컨')
    Squid = models.BooleanField(default=False, verbose_name='오징어')
    Cheese = models.BooleanField(default=False, verbose_name='치즈')
    Tomato = models.BooleanField(default=False, verbose_name='토마토')
    # 야채류는?

    ### 소스
