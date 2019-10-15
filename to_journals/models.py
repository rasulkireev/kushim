from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

class to_journal(models.Model):
    name = models.CharField(max_length = 40)
    slug = AutoSlugField(populate_from='name')
    date_created = models.DateTimeField(auto_now_add=True)
    journal_user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.journal_user) + " " + self.name

    def get_absolute_url(self):
        return reverse('to-journals')


class to_journal_entry(models.Model):
    body = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)

    parent_journal = models.ForeignKey(
    to_journal,
    on_delete=models.CASCADE,
    related_name="entries")

    journal_user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )


    def __str__(self):
        return str(self.parent_journal) + " " + str(self.entry_date)

    def get_absolute_url(self):
         return reverse('to_journals', args=[str(self.slug)])
