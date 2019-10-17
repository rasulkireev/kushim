from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import to_journal, to_journal_entry
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import get_object_or_404



class CreateToJournal(LoginRequiredMixin, CreateView):
    model = to_journal
    template_name = 'to_journals/to_journal_list.html'
    fields = ('journal_name',)

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
        current_journal = to_journal.objects.get(journal_user=self.request.user, slug=self.kwargs['slug'])
        return reverse_lazy('to-journal-entries', str(current_journal.slug))

    def form_valid(self, form):
        current_journal = to_journal.objects.get(journal_user=self.request.user, slug=self.kwargs['slug'])
        form.instance.journal_user = self.request.user
        form.instance.journal_name = current_journal
        return super(ToJournalEntriesList, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ToJournalEntriesList, self).get_context_data(**kwargs)
        context['to_journal_entries'] = to_journal_entry.objects.all()
        return context
