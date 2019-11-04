from django.urls import path
from .views import CreateToJournal, ToJournalEntriesList, DeleteJournal, RenameJournal, EditJournalEntry


urlpatterns = [
    path('', CreateToJournal.as_view(), name='to-journals'),
    path('<slug:slug>', ToJournalEntriesList.as_view(), name='to-journal-entries'),
    path('<slug:slug>/<int:id>/delete', DeleteJournal.as_view(), name='delete-journal'),
    path('<slug:slug>/<int:id>/rename', RenameJournal.as_view(), name='rename-journal'),
    path('<int:id>/edit-entry', EditJournalEntry.as_view(), name='edit-journal-entry'),
]
