from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    "комменты которые может создавать пользователь"
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
