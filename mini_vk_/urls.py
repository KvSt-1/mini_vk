"Определяет схемы URL для mini_vk_"
from django.urls import path
from . import views

app_name = 'mini_vk_'
urlpatterns = [
    #Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком профилей
    path('profiles/', views.profiles, name='profiles'),
    # Cтраница конкретного пользователя
    path('profiles/<int:profile_id>/',views.profile, name = 'profile'),
    #Редактирование профил
    path('profiles/<int:profile_id>/edit/',views.edit_profile, name = 'edit_profile'),
    #Редактирование поста
    path('post/<int:post_id>/edit/',views.edit_post, name='edit_post')
]