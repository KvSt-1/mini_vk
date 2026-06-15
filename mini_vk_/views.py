from django.shortcuts import render

def index(request):
    "Домашиняя страница приложения mini_vk"
    return render(request, 'mini_vk_/index.html')
