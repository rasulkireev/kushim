from django.urls import path
from .views import UpgradePageView, charge

urlpatterns = [
    path('success/', charge, name='charge-success'),
    path('', UpgradePageView.as_view(), name='upgrade'),
]