from django.db import models


class Menu(models.Model):
    image = models.ImageField(upload_to='static/img/BURGERKING_MENU/Burger/', verbose_name='이미지', null=True, blank=True)
    name = models.CharField(max_length=25, verbose_name='메뉴명')
    price = models.IntegerField(verbose_name='가격', default=10000)
    calorie = models.FloatField(verbose_name='칼로리', default=100.5)

class MenuTable(models.Model):
    # base information
    menu_name = models.CharField(max_length=25, verbose_name='메뉴명')
    price = models.IntegerField(default=5000, verbose_name='가격')    # integer? float? char?
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    info = models.TextField(default="맛있다.", verbose_name='정보')
    rank = models.IntegerField(default=99, verbose_name='인기순위')
    spicy = models.IntegerField(default=0, verbose_name='맵기')

    # nutrition information
    N_calories = models.IntegerField(default=0, verbose_name='영양성분 : 칼로리')
    N_protein = models.IntegerField(default=0, verbose_name='영양성분 : 단백질')
    N_sodium = models.IntegerField(default=0, verbose_name='영양성분 : 나트륨')
    N_sugars = models.FloatField(default=0, verbose_name='영양성분 : 설탕')
    N_saturated_fat = models.FloatField(default=0, verbose_name='영양성분 : 포화지방')

    # allergy
    A_milk = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 우유')
    A_chicken = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 치킨')
    A_pork = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 돼지')
    A_beef = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 소')
    A_egg = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 난류')
    A_squid = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 오징어')
    A_tomato = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 토마토')
    A_clam = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 조개')
    A_shrimp = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 새우')

    # ingredients
    I_sliced_cheese = models.IntegerField(default=0, verbose_name='재료 : 얇게 썬 치즈')
    I_shredded_cheese = models.IntegerField(default=0, verbose_name='재료 : 잘게 썬 치즈')
    I_pickle = models.IntegerField(default=0, verbose_name='재료 : 피클')
    I_jalapeno = models.IntegerField(default=0, verbose_name='재료 : 할라피뇨')
    I_whole_shrimp = models.IntegerField(default=0, verbose_name='재료 : 통새우')
    I_bacon = models.IntegerField(default=0, verbose_name='재료 : 베이컨')
    I_tomato = models.IntegerField(default=0, verbose_name='재료 : 토마토')
    I_garlic_chip = models.IntegerField(default=0, verbose_name='재료 : 마늘 칩')
    I_lettuce = models.IntegerField(default=0, verbose_name='재료 : 상추')
    I_onion = models.IntegerField(default=0, verbose_name='재료 : 양파')
    I_hashbrown = models.IntegerField(default=0, verbose_name='재료 : 해쉬브라운')

    # sauce
    S_mayo = models.BooleanField(default=False, null=True, verbose_name='소스 : 마요네즈')
    S_bulgogi = models.BooleanField(default=False, null=True, verbose_name='소스 : 불고기')
    S_barbecue = models.BooleanField(default=False, null=True, verbose_name='소스 : 바비큐 ')
    S_ketchup = models.BooleanField(default=False, null=True, verbose_name='소스 : 캐첩')
    S_diablo = models.BooleanField(default=False, null=True, verbose_name='소스 : 디아블로 ')
    S_spicy_tomato = models.BooleanField(default=False, null=True, verbose_name='소스 : 매운 토마토 ')
    S_cheese = models.BooleanField(default=False, null=True, verbose_name='소스 : 치즈 ')
    S_tartar = models.BooleanField(default=False, null=True, verbose_name='소스 : 타르타르 ')
    S_baconjam = models.BooleanField(default=False, null=True, verbose_name='소스 : 베이컨잼')
    S_mustard = models.BooleanField(default=False, null=True, verbose_name='소스 : 머스타드')

    # patty
    P_beef = models.IntegerField(default=0, verbose_name='패티 : 소고기')
    P_shrimp = models.IntegerField(default=0, verbose_name='패티 : 새우')
    P_chicken = models.IntegerField(default=0, verbose_name='패티 : 치킨')
    P_steak = models.IntegerField(default=0, verbose_name='패티 : 스테이크')


    def __str__(self):
        return self.menu_name