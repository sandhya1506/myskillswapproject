from django.db import models
from django.contrib.auth.models import User 

CATEGORIES =  [
        ('TC', 'Technical'),
        ('CR', 'Crafts'),
        ('LN', 'Languages'),
        ('HI', 'Home Improvement'),
        ('HB', 'Health & Beauty'),
        ('OT', 'Other')
]

class AddSkills(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='OT')
    availability = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=200) # very big, please make it look better
    
    def __str__(self):
        return self.title
    
class RequestSkills(models.Model):
   # user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='OT')
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.category


