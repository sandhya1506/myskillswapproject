from django.contrib import admin
from .models import User, UserProfile
from forms import UserProfileForm, Form


# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserProfileForm)
admin.site.register(Form)
