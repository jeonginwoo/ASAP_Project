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
    image = models.CharField(max_length=50, verbose_name='이미지')
    info = models.TextField(default="맛있다.", verbose_name='정보')
    rank = models.IntegerField(default=99, verbose_name='인기순위')
    spicy = models.IntegerField(default=0, verbose_name='맵기')

    # nutrition information
    calories = models.IntegerField(default=0, verbose_name='영양성분 : 칼로리')
    protein = models.IntegerField(default=0, verbose_name='영양성분 : 단백질')
    sodium = models.IntegerField(default=0, verbose_name='영양성분 : 나트륨')
    sugars = models.FloatField(default=0, verbose_name='영양성분 : 설탕')
    saturated_fat = models.FloatField(default=0, verbose_name='영양성분 : 포화지방')

    # allergy
    Amilk = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 우유')
    AChicken = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 치킨')
    Apork = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 돼지')
    Abeef = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 소')
    Aegg = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 난류')
    Asquid = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 오징어')
    ATomato = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 토마토')
    Aclam = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 조개')
    Ashrimp = models.BooleanField(default=False, null=True, verbose_name='알레르기 : 새우')

    # ingredients
    sliced_cheese = models.IntegerField(default=0, verbose_name='재료 : 얇게 썬 치즈')
    shredded_cheese = models.IntegerField(default=0, verbose_name='재료 : 잘게 썬 치즈')
    pickle = models.IntegerField(default=0, verbose_name='재료 : 피클')
    jalapeno = models.IntegerField(default=0, verbose_name='재료 : 할라피뇨')
    whole_shrimp = models.IntegerField(default=0, verbose_name='재료 : 통새우')
    bacon = models.IntegerField(default=0, verbose_name='재료 : 베이컨')
    bulgogi = models.IntegerField(default=0, verbose_name='재료 : 불고기')
    barbecue = models.IntegerField(default=0, verbose_name='재료 : 바비큐')
    lettuce = models.IntegerField(default=0, verbose_name='재료 : 상추')
    onion = models.IntegerField(default=0, verbose_name='재료 : 양파')
    hashbrown = models.IntegerField(default=0, verbose_name='재료 : 해쉬브라운')

    # sauce
    mayo = models.BooleanField(default=False, null=True, verbose_name='소스 : 마요네즈')
    bulgogi = models.BooleanField(default=False, null=True, verbose_name='소스 : 불고기')
    barbecue = models.BooleanField(default=False, null=True, verbose_name='소스 : 바비큐 ')
    ketchup = models.BooleanField(default=False, null=True, verbose_name='소스 : 캐첩')
    diablo = models.BooleanField(default=False, null=True, verbose_name='소스 : 디아블로 ')
    spicy_tomato = models.BooleanField(default=False, null=True, verbose_name='소스 : 매운 토마토 ')
    cheese = models.BooleanField(default=False, null=True, verbose_name='소스 : 치즈 ')
    tartar = models.BooleanField(default=False, null=True, verbose_name='소스 : 타르타르 ')
    baconjam = models.BooleanField(default=False, null=True, verbose_name='소스 : 베이컨잼')
    mustard = models.BooleanField(default=False, null=True, verbose_name='소스 : 머스타드')

    # patty
    Pbeef = models.IntegerField(default=0, verbose_name='패티 : 소고기')
    Pshrimp = models.IntegerField(default=0, verbose_name='패티 : 새우')
    Pchicken = models.IntegerField(default=0, verbose_name='패티 : 치킨')
    Psteak = models.IntegerField(default=0, verbose_name='패티 : 스테이크')


    def __str__(self):
        return self.menu_name