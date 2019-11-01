from django.urls import path
from .views import CreateContact


urlpatterns = [
    path('', CreateContact.as_view(), name='contacts'),
]
