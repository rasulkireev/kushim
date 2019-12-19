from django.urls import path
from .views import CreateList, CreateListEntry, DeleteList, RenameList, EditListEntry, DeleteGardenEntry


urlpatterns = [
    path('', CreateList.as_view(), name='lists'),
    path('<slug:slug>', CreateListEntry.as_view(), name='list-entries'),

    path('<slug:slug>/<int:id>/delete', DeleteList.as_view(), name='delete-list'),
    path('<slug:slug>/<int:id>/rename', RenameList.as_view(), name='rename-list'),
    
    path('<int:id>/edit-garden-item', EditListEntry.as_view(), name='edit-list-entry'),
    path('<int:id>/delete-garden-item', DeleteGardenEntry.as_view(), name='delete-garden-entry'),
]
