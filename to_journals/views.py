from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import to_journal, to_journal_entry, JournalForm
from django.urls import reverse



class CreateToJournal(LoginRequiredMixin, CreateView):
    model = to_journal
    template_name = 'to_journals/to_journal_list.html'
    form_class = JournalForm

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.journal_user = self.request.user
        return super(CreateToJournal, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateToJournal, self).get_context_data(**kwargs)
        context['to_journals'] = to_journal.objects.filter(journal_user=self.request.user)
        return context


class ToJournalEntriesList(LoginRequiredMixin, CreateView):
    model = to_journal_entry
    template_name = 'to_journals/to_journal_entries_list.html'
    fields = ('body',)

    def get_success_url(self):
        return reverse('to-journal-entries', kwargs={'slug':self.object.journal_name.slug})

    def form_valid(self, form):
        current_journal = to_journal.objects.get(journal_user=self.request.user, slug=self.kwargs['slug'])
        form.instance.journal_user = self.request.user
        form.instance.journal_name = current_journal
        return super(ToJournalEntriesList, self).form_valid(form)

    def get_context_data(self, **kwargs):
        current_journal = to_journal.objects.get(journal_user=self.request.user, slug=self.kwargs['slug'])
        context = super(ToJournalEntriesList, self).get_context_data(**kwargs)
        context['to_journal_entries'] = to_journal_entry.objects.filter(journal_user=self.request.user, journal_name=current_journal)
        return context
