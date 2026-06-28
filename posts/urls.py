"Определяет схемы URL для users"
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('profiles/<int:profile_id>/',views.user_post_view, name = 'user_posts'),
    #Редактирование поста
    path('post/<int:post_id>/edit/',views.edit_post, name='edit_post')
]