from django.shortcuts import render, get_object_or_404, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile
from .serializers import ProfileSerializer

def index(request):
    "Домашняя страница приложения core_mini_vk"
    return render(request, 'users/index.html')

@api_view(['GET'])
def profile_list(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)

    return Response(serializer.data)


#def profiles(request):
    "Выводит список профилей"
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

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




