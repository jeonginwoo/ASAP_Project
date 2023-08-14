from django.db import models


class Menu(models.Model):
    image = models.ImageField(verbose_name='이미지',null = True, blank= True)
    name = models.CharField(max_length = 25, verbose_name='메뉴명')
    price = models.IntegerField(verbose_name='가격', default=10000)
    calorie = models.FloatField(verbose_name='칼로리', default=100.5)
    
class test_Menu_Set(models.Model):
    menu_name = models.CharField(max_length=45, primary_key=True)
    weight = models.IntegerField(null=True)
    calories = models.IntegerField(null=True)
    protein = models.IntegerField(null=True)
    sodium = models.IntegerField(null=True)
    sugars = models.IntegerField(null=True)
    saturated_fat = models.IntegerField(null=True)
    caffeine = models.IntegerField(null=True)
    milk = models.IntegerField(null=True)
    pork = models.IntegerField(null=True)
    tomato = models.IntegerField(null=True)
    beef = models.IntegerField(null=True)
    egg = models.IntegerField(null=True)
    squid = models.IntegerField(null=True)
    lettuce = models.IntegerField(null=True)
    mayo = models.IntegerField(null=True)
    sliced_cheese = models.IntegerField(null=True)
    shredded_cheese = models.IntegerField(null=True)
    pickle = models.IntegerField(null=True)
    jalapeno = models.IntegerField(null=True)
    whole_shrimp = models.IntegerField(null=True)
    bacon = models.IntegerField(null=True)
    onion = models.IntegerField(null=True)
    bulgogi = models.IntegerField(null=True)
    barbecue = models.IntegerField(null=True)
    ketchup = models.IntegerField(null=True)
    diablo = models.IntegerField(null=True)
    spicy_tomato = models.IntegerField(null=True)
    cheese = models.IntegerField(null=True)
    tartar = models.IntegerField(null=True)

    def __str__(self):
        return self.menu_name



