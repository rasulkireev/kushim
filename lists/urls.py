from django.urls import path
from .views import CreateList, CreateListEntry, DeleteList, RenameList, EditListEntry


urlpatterns = [
    path('', CreateList.as_view(), name='lists'),
    path('<slug:slug>', CreateListEntry.as_view(), name='list-entries'),
    path('<slug:slug>/delete', DeleteList.as_view(), name='delete-list'),
    path('<slug:slug>/rename', RenameList.as_view(), name='rename-list'),
    path('<int:id>/edit-entry', EditListEntry.as_view(), name='edit-entry'),
]
