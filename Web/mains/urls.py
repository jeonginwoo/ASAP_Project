from django.urls import path

from . import views

app_name = 'mains'

urlpatterns = [
    path('', views.index, name='index'),
    path('Menu/<str:menu_key>/', views.MenuDetailView.as_view(), name='menu-detail'),
    path('purchase/', views.purchase, name='purchase'),
    path('speechrecognize/', views.speechRecognition, name="speechRecognition"),

    path('burgerlist/', views.testBurger, name='testBurger'),
    path('sidelist/', views.testSide, name='testSide'),
    path('ddlist/', views.testDD, name='testDD'),
    path('menuReco/', views.menuQuery, name='testQuery'),
]