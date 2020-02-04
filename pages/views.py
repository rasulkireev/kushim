from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from lists.models import List, ListForm
from to_journals.models import to_journal, JournalForm
from network.models import Contact
from network.forms import ContactForm

class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = 'account_login'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gardens'] = List.objects.filter(list_owner=self.request.user)[:3]
        context['garden_form'] = ListForm
        
        context['contacts'] = Contact.objects.filter(contact_owner=self.request.user)[:3]
        context['network_form'] = ContactForm

        context['journals'] = to_journal.objects.filter(journal_user=self.request.user)[:3]
        context['journal_form'] = JournalForm

        return context

class LoggedInHomePageView(TemplateView):
    template_name = 'home.html'

class UpgradeAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'upgrade_account.html'
