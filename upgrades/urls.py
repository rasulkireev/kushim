from django.urls import path
from .views import UpgradePageView, charge

urlpatterns = [
    path('', UpgradePageView.as_view(), name='upgrade'),
    path('success/', charge, name='charge-success'),
]