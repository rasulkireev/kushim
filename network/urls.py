from django.urls import path
from .views import CreateContact, CreateContactLog


urlpatterns = [
    path('', CreateContact.as_view(), name='contacts'),
    path('<int:id>', CreateContactLog.as_view(), name='contact-detail'),
]
