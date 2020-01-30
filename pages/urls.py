from django.contrib import admin
from django.urls import path
from .views import HomePageView, UpgradeAccountView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
