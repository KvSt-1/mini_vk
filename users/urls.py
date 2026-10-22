"Определяет схемы URL для users"
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком профилей
    path('api/profiles/', views.profile_list, name='profile_list'),
    # Cтраница конкретного пользователя
    path('profiles/<int:profile_id>/',views.profile, name = 'profile'),
    #Редактирование профил
    path('profiles/<int:profile_id>/edit/',views.edit_profile, name = 'edit_profile'),

]