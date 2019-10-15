from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('<str:user>', HomePageView.as_view(), name='logged-in-home'),
]
