from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm

from .models import CustomUser

class CustomLoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'block appearance-none w-full bg-white border border-grey-light hover:border-grey px-2 py-2 rounded shadow'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'block appearance-none w-full bg-white border border-grey-light hover:border-grey px-2 py-2 rounded shadow'}))
    

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
            super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            
            for fieldname in ['username', 'email', 'password1', 'password2']:
                self.fields[fieldname].help_text = None
                self.fields[fieldname].widget.attrs.update({'class':'block appearance-none w-full bg-white border border-grey-light hover:border-grey px-2 py-2 rounded shadow'})

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_profile_image')



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

