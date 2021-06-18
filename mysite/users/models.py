from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='admin/default.jpg',upload_to='profile_pics')
    bio = models.CharField(max_length=50, null=True, blank=True)
    timespent = models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.user.username} profile'
