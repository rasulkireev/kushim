from django.urls import path
from .views import SignUpView
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(authentication_form=CustomLoginForm)),

]
