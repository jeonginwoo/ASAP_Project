from django.urls import path

from . import views

app_name = 'mains'

urlpatterns = [
    # path('Menu/<str:menu_key>/', views.MenuDetailView.as_view(), name='menu-detail'),
    path('purchase/', views.purchase, name='purchase'),
    path('speechrecognize/', views.speechRecognition, name="speechRecognition"),
    path('textinput/', views.textInput, name='textInput'),

    # 메뉴 리스트 확인 페이지
    path('burgerlist/', views.testBurger, name='testBurger'),
    path('sidelist/', views.testSide, name='testSide'),
    path('ddlist/', views.testDD, name='testDD'),
    path('menuReco/',views.test, name = 'test'),

    # 추천 리스트 페이지
    
]
