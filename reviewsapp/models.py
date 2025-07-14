from django.db import models
from user_authentication.models import UserProfile

class Review(models.Model):
    name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey('skills.AddSkills', related_name='reviews', on_delete=models.CASCADE)
    email = models.EmailField()
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating})"
