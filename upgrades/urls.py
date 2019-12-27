from django.urls import path
from .views import UpgradePageView

urlpatterns = [
    path('', UpgradePageView.as_view(), name='upgrade'),
]