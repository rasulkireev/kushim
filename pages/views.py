from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = 'account_login'
    template_name = 'home.html'

class LoggedInHomePageView(TemplateView):
    template_name = 'home.html'

class UpgradeAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'upgrade_account.html'
