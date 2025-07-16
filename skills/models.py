from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

CATEGORIES =  [
        ('TC', 'Technical'),
        ('CR', 'Crafts'),
        ('LN', 'Languages'),
        ('OT', 'Other')
]

class AddSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='OT')
    availability = models.BooleanField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    average_rating = models.FloatField(default=0.0)
    
    # @property
    # def calculated_rating(self):
    #     return self.reviews.aggregate(Avg('rating'))['avg'] or 0

    def __str__(self):
        return self.title
    
class RequestSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='OT')
    location = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.title


