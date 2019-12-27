from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    dob = models.DateField(blank=True, null=True)
    user_profile_image = models.ImageField(blank=True, upload_to='user-profile-images/')

