from django.views.generic.base import TemplateView

class UpgradePageView(TemplateView):
    template_name = 'upgrades/to_pro.html'