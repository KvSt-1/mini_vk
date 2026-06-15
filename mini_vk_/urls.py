"Определяет схемы URL для mini_vk_"
from django.urls import path
from . import views

app_name = 'mini_vk_'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
]