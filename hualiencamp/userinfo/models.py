from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    # 一對一的連接到內建的 User 模型
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True,max_length=75)
    birthdate = models.DateField(null=True, blank=True)
    

    def __str__(self):
        return self.user.username