from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class LoggedInHomePageView(TemplateView):
    template_name = 'home.html'
