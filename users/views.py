from django.shortcuts import render, get_object_or_404, redirect

from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import viewsets

def index(request):
    "Домашняя страница приложения core_mini_vk"
    return render(request, 'users/index.html')

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

def profile(request, profile_id):
    "Выводит конкретный профиль"
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'users/profile.html',
                  {'profile': profile})

def edit_profile(request, profile_id):
    "редактирование профиля"
    profile = Profile.objects.get(id=profile_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile', profile_id = profile_id)
    else:
        form = ProfileForm(instance=profile)
    return render(request,'users/edit_profile.html', {'form':form})




