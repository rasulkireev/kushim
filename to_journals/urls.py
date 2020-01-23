from django.urls import path
from .views import CreateToJournal, ToJournalEntriesList, DeleteJournal, EditJournal, EditJournalEntry, DeleteJournalEntry


urlpatterns = [
    path('', CreateToJournal.as_view(), name='to-journals'),
    path('<slug:slug>', ToJournalEntriesList.as_view(), name='to-journal-entries'),

    path('<slug:slug>/<int:id>/delete', DeleteJournal.as_view(), name='delete-journal'),
    path('<slug:slug>/<int:id>/edit', EditJournal.as_view(), name='edit-journal'),

    path('<int:id>/edit-entry', EditJournalEntry.as_view(), name='edit-journal-entry'),
    path('<int:id>/delete-entry', DeleteJournalEntry.as_view(), name='delete-journal-entry'),
]
