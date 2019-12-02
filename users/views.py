from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView
from .models import CustomUser
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class CustomUserView(ListView):
    model = CustomUser
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        current_user = CustomUser.objects.get(user=self.request.user)

        context = super(CustomUserView, self).get_context_data(**kwargs)
        context['user_profile_image'] = current_user.user_profile_image
        return context

class EditCustomUser(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'user'
    fields = ('user_profile_image', 'dob')
    
    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        current_user = CustomUser.objects.get(user=self.request.user)
        return super(EditContact, self).form_valid(form)

