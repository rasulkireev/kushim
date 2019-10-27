from django.urls import path
from .views import CreateToJournal, ToJournalEntriesList, DeleteJournal, RenameJournal


urlpatterns = [
    path('', CreateToJournal.as_view(), name='to-journals'),
    path('<slug:slug>', ToJournalEntriesList.as_view(), name='to-journal-entries'),
    path('<slug:slug>/delete', DeleteJournal.as_view(), name='delete-journal'),
    path('<slug:slug>/rename', RenameJournal.as_view(), name='rename-journal'),
]
