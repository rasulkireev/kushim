from django.urls import path
from .views import CreateToJournal, ToJournalEntriesList, DeleteJournal


urlpatterns = [
    path('', CreateToJournal.as_view(), name='to-journals'),
    path('<slug:slug>', ToJournalEntriesList.as_view(), name='to-journal-entries'),
    path('<str:journal_user>/<slug:slug>/delete', DeleteJournal.as_view(), name='delete-journal'),
]
