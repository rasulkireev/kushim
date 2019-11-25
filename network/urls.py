from django.urls import path
from .views import CreateContact, CreateContactLog, EditContact


urlpatterns = [
    path('', CreateContact.as_view(), name='contacts'),
    path('<int:id>', CreateContactLog.as_view(), name='contact-detail'),
    path('<int:id>/edit', EditContact.as_view(), name='edit-contact'),
]
