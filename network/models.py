from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class Contact(models.Model):
    contact_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    contact_id = AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)

    Female = 'Female'
    Male = 'Male'
    GENDER = [
        (Female, 'Female'),
        (Male, 'Male'),
    ]
    gender = models.CharField(
        max_length=20,
        choices=GENDER,
        blank = True
    )

    nickname = models.CharField(max_length = 30, blank=True)
    email = models.EmailField()
    tags = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to='profile-images/', blank=True)
    how_you_met = models.TextField(blank=True)
    current_title = models.CharField(max_length=200, blank=True)
    current_employer = models.CharField(max_length=200, blank=True)
    current_location = models.CharField(max_length=200, blank=True)
    when_to_contact = models.DurationField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=31, blank=True)



    def __str__(self):
        return str(self.journal_user) + " " + self.journal_name
