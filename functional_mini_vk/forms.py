from django import forms
from .models import Profile,Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city','bio','birth_date']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']