from django.urls import path
from .views import CreateContact, CreateContactLog, EditContact, CreateContactContact, EditContactLog, DeleteContactLog


urlpatterns = [
    path('', CreateContact.as_view(), name='contacts'),
    path('<int:contact_id>', CreateContactLog.as_view(), name='contact-detail'),
    
    path('<int:id>/edit', EditContact.as_view(), name='edit-contact'),
    path('<int:id>/editcontact', CreateContactContact.as_view(), name='edit-contact-contacts'),

    path('<int:id>/editlog', EditContactLog.as_view(), name='edit-contact-log'),
    path('<int:id>/deletelog', DeleteContactLog.as_view(), name='delete-contact-log'),
]
