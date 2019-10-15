from django.urls import path
from .views import CreateToJournal, ToJournalEntriesList


urlpatterns = [
    path('', CreateToJournal.as_view(), name='to-journals'),
    path('<slug:slug>', ToJournalEntriesList.as_view(), name='to-journal-entries'),
]
