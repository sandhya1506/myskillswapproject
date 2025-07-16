from django.db import models
from django.db.models import Avg
from user_authentication.models import UserProfile

CATEGORIES =  [
        ('TC', 'Technical'),
        ('CR', 'Crafts'),
        ('LN', 'Languages'),
        ('HI', 'Home Improvement'),
        ('HB', 'Health & Beauty'),
        ('OT', 'Other')
]

class AddSkills(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='OT')
    availability = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=200) # very big, please make it look better
    average_rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title
    
class RequestSkills(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='OT')
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    

    def __str__(self):
        return self.category


@property
def average_rating(self):
    return self.reviewsapp.aggregate(Avg('rating'))['rating__avg'] or 0