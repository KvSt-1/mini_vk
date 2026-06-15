from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile,Post
from .forms import PostForm,ProfileForm

def index(request):
    "Домашняя страница приложения mini_vk"
    return render(request, 'mini_vk_/index.html')

def profiles(request):
    "Выводит список профилей"
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'mini_vk_/profiles.html', context)

def profile(request, profile_id):
    "Выводит конкретный профиль"
    profile = get_object_or_404(Profile, id=profile_id)
    posts = Post.objects.filter(author=profile.user)
    return render(request, 'mini_vk_/profile.html',
                  {'profile': profile
                   , 'posts': posts})

def edit_profile(request, profile_id):
    "редактирование профиля"
    profile = Profile.objects.get(id=profile_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('mini_vk_:profile', profile_id = profile_id)
    else:
        form = ProfileForm(instance=profile)
    return render(request,'mini_vk_/edit_profile.html', {'form':form})

def edit_post(request, post_id):
    "Редактирование Поста"
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('mini_vk_:profile', profile_id=post.author.profile.id)
    else:
        form = PostForm(instance=post)
    return render(request,'mini_vk_/edit_post.html',{'form':form})



