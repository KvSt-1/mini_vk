from django.shortcuts import render, get_object_or_404
from .models import Profile,Post

def index(request):
    "Домашняя страница приложения mini_vk"
    return render(request, 'mini_vk_/index.html')

def profiles(request):
    "Выводит список профилей"
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'mini_vk_/profiles.html', {'profiles': profiles})

def profile(request, profile_id):
    "Выводит конкретный профиль"
    profile = get_object_or_404(Profile, id=profile_id)
    posts = Post.objects.filter(author=profile.user)
    return render(request, 'mini_vk_/profile.html',
                  {'profile': profile
                   , 'posts': posts})
