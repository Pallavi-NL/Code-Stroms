from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # For user authentication

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()  # Store event image URLs
    date = models.DateTimeField(auto_now_add=True)  # Auto-generated event date

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    bio = models.TextField(blank=True, null=True)  
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  

    def __str__(self):
        return self.user.username
