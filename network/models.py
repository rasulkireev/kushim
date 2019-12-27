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
    contact_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)

    nickname = models.CharField(max_length = 30, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to='profile-images/', blank=True)
    how_you_met = models.TextField(blank=True)
    description = models.TextField(blank=True)
    current_location = models.CharField(max_length=200, blank=True)
    when_to_contact = models.DurationField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    title = models.CharField(max_length=200, blank=True)
    employer = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('contacts')


class ContactContact(models.Model):
    contact_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=200, blank=True)
    contact_value = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.contact_type) + ": " + str(self.contact_value) + " - " + str(self.contact_id)


class ContactLog(models.Model):
    contact_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    Gift_Ideas = 'Gift Ideas'
    Notes = 'Notes'
    Conversations = 'Conversations'
    LOG_TYPE = [
        (Gift_Ideas, 'Gift Ideas'),
        (Notes, 'Notes'),
        (Conversations, 'Conversations'),
    ]
    log_type = models.CharField(
    choices=LOG_TYPE,
        max_length=20,
        default=Notes,
    )

    body = models.TextField()
    support_image = models.ImageField(blank=True, upload_to='network-log-support-images/')

    def __str__(self):
        return str(self.contact_id) + ": " + self.log_type
