from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


class to_journal(models.Model):
    journal_name = models.CharField(max_length = 40)
    slug = AutoSlugField(populate_from='journal_name')
    date_created = models.DateTimeField(auto_now_add=True)
    journal_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.journal_user) + " " + self.journal_name

    def get_absolute_url(self):
        return reverse('to-journals')


class to_journal_entry(models.Model):
    body = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    journal_name = models.ForeignKey(to_journal, on_delete=models.CASCADE,)
    journal_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.journal_name) + " " + str(self.entry_date)

    def get_absolute_url(self):
        return reverse('to-journal-entries', args=(self.slug))
