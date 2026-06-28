from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    "профиль пользователя"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank = True)
    city = models.CharField(null=True, blank = True, max_length = 100)
    bio = models.TextField(null=True, blank = True)

    def __str__(self):
        return self.user.username


