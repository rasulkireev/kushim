from django.urls import path
from .views import CreateList, CreateListEntry, DeleteList, EditGarden, EditListEntry, DeleteGardenEntry


urlpatterns = [
    path('', CreateList.as_view(), name='lists'),
    path('<slug:slug>', CreateListEntry.as_view(), name='list-entries'),

    path('<slug:slug>/<int:id>/delete', DeleteList.as_view(), name='delete-list'),
    path('<slug:slug>/<int:id>/edit', EditGarden.as_view(), name='edit-list'),
    
    path('<int:id>/edit-garden-item', EditListEntry.as_view(), name='edit-list-entry'),
    path('<int:id>/delete-garden-item', DeleteGardenEntry.as_view(), name='delete-garden-entry'),
]
