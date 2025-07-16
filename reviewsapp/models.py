from django.db import models
from user_authentication.models import UserProfile
from skills.models import AddSkills

class Review(models.Model):
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='given_reviews')
    reviewee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='received_reviews')
    skill = models.ForeignKey(AddSkills, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.username} → {self.reviewee.username} ({self.rating})"
