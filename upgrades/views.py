import stripe

from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib.auth.models import Permission
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY

class UpgradePageView(TemplateView):
    template_name = 'upgrades/to_pro.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_PUBLIC_KEY
        return context


def charge(request):

    # Get the permission
    journal_permission = Permission.objects.get(codename='journal-pro')
    network_permission = Permission.objects.get(codename='network-pro')
    garden_permission = Permission.objects.get(codename='garden-pro')
    
    # Get user
    u = request.user

    # Add to user's permission set
    u.user_permissions.add(journal_permission)
    u.user_permissions.add(network_permission)
    u.user_permissions.add(garden_permission)


    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=2500,
            currency='usd',
            description='Getting Pro Access',
            source=request.POST['stripeToken']
        )
        return render(request, 'upgrades/success.html')