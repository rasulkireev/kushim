from django.urls import path
from .views import CreateContact, CreateLog


urlpatterns = [
    path('', CreateContact.as_view(), name='contacts'),
    path('<int:id>', CreateLog.as_view(), name='contact-detail'),
]
