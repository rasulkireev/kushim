from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import to_journal, to_journal_entry
from django.urls import reverse_lazy



class CreateToJournal(LoginRequiredMixin, CreateView):
    model = to_journal
    template_name = 'to_journals/to_journal_list.html'
    fields = ('name',)

    def form_valid(self, form):
        form.instance.journal_user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateToJournal, self).get_context_data(**kwargs)
        context['to_journals'] = to_journal.objects.filter(journal_user=self.request.user)
        return context




# class ToJournalsListView(ListView):
#     model = to_journal
#     template_name = 'to_journals/to_journal_list.html'
#
#     def get_queryset(self):
#         return to_journal.objects.filter(journal_user=self.request.user)


class ToJournalEntriesList(LoginRequiredMixin, CreateView):
    model = to_journal_entry
    template_name = 'to_journals/to_journal_entries_list.html'
    fields = ('body',)

    def form_valid(self, form):
        form.instance.journal_user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ToJournalEntriesList, self).get_context_data(**kwargs)
        context['to_journal_entries'] = to_journal_entry.objects.filter(journal_user=self.request.user)
        return context

    # def get_queryset(self):
    #     return to_journal_entry.objects.filter(parent_journal=self)
