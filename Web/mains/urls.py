from django.urls import path

from . import views

app_name = 'mains'

urlpatterns = [
    path('Menu/<str:menu_key>/', views.MenuDetailView.as_view(), name='menu-detail'),
    path('purchase/', views.purchase, name='purchase'),
    path('speechrecognize/', views.speechRecognition, name="speechRecognition"),
    path('textinput/', views.textInput, name='textInput'),
    
    path('test/', views.testTable, name='testTable'),
]