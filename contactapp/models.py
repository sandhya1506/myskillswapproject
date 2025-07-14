from django.db import models
from user_authentication.models import UserProfile

# Create your models here.


class ContactMessage(models.Model):
    sender= models.ForeignKey(UserProfile, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(UserProfile, related_name='recieved_messages', on_delete=models.CASCADE)
    skill = models.ForeignKey('skills.AddSkills', on_delete=models.CASCADE)
    email= models.EmailField()
    message= models.TextField()
    submitted_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.recipient} asking for ({self.skill})"
