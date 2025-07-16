from django.db import models
<<<<<<< HEAD
from user_authentication.models import UserProfile

class Review(models.Model):
    name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey('skills.AddSkills', related_name='reviews', on_delete=models.CASCADE)
    email = models.EmailField()
    rating = models.PositiveIntegerField()
=======
from django.contrib.auth.models import User

class Skill(models.Model):  
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_reviews')
    reviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reviews')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    rating = models.IntegerField()
>>>>>>> origin/reviewsfeature
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.username} → {self.reviewee.username} ({self.rating})"
