from django.urls import path
from .views import SignUpView, EditCustomUser
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(authentication_form=CustomLoginForm), name='login'),
    path('edit-account/<int:pk>', EditCustomUser.as_view(), name='edit-account'),
    ]
