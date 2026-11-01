"Определяет схемы URL для users"
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    # Cтраница конкретного пользователя
    path('profiles/<int:profile_id>/',views.profile, name = 'profile'),
    #Редактирование профил
    path('profiles/<int:profile_id>/edit/',views.edit_profile, name = 'edit_profile'),

]