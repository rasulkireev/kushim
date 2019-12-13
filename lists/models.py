from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

class List(models.Model):
    list_name = models.CharField(max_length = 40)
    slug = AutoSlugField(populate_from='list_name',always_update=True)
    date_created = models.DateTimeField(auto_now_add=True)
    list_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.list_owner) + " " + self.list_name

    def get_absolute_url(self):
        return reverse('lists')

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['list_name']


class ListEntry(models.Model):
    body = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    list_name = models.ForeignKey(List, on_delete=models.CASCADE,)
    list_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    support_image = models.ImageField(blank=True, upload_to='list-support-images/')

    def __str__(self):
        return str(self.list_name) + " " + str(self.entry_date)

    def get_absolute_url(self):
        current_list = List.objects.get(journal_user=self.request.user, slug=self.kwargs['slug'])
        return reverse('list-entries', args=current_journal)
