from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE, )

    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

