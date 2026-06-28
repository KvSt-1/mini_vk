from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from users.models import Profile
from .forms import PostForm

def user_post_view(request,profile_id):
    "Выводит конкретный профиль"
    profile = get_object_or_404(Profile, id=profile_id)
    posts = Post.objects.filter(author=profile.user)
    return render(request, 'users/profile.html',
                  {'profile': profile
                      , 'posts': posts})

def edit_post(request, post_id):
    "Редактирование Поста"
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('users:profile', profile_id=post.author.profile.id)
    else:
        form = PostForm(instance=post)
    return render(request,'users/edit_post.html',{'form':form})
