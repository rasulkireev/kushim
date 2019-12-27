from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.functional import cached_property

from djstripe.utils import subscriber_has_active_subscription



class CustomUser(AbstractUser):
    dob = models.DateField(blank=True, null=True)
    user_profile_image = models.ImageField(blank=True, upload_to='user-profile-images/')

    @cached_property
    def has_active_subscription(self):
        """Checks if a user has an active subscription."""
        return subscriber_has_active_subscription(self)
