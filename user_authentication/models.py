from django.db import models
from django.contrib.auth.models import User
from user_authentication.forms import Form 

class UserProfile(models.model):
    user = models.OneToOneField(User)

    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

