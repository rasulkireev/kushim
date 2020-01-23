from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import to_journal, to_journal_entry, JournalForm
from .forms import EditJournal
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http.response import HttpResponseRedirect


class CreateToJournal(LoginRequiredMixin, CreateView):
    model = to_journal
    template_name = 'to_journals/to_journal_list.html'
    form_class = JournalForm

    def get_success_url(self):
        return reverse('home')

    def is_limit_reached(self):
        return to_journal.objects.filter(journal_user=self.request.user).count() >= 3

    def has_permission(self):
        return self.request.user.has_perm('to_journals.journal-pro')

    def post(self, request, *args, **kwargs):
        if self.is_limit_reached() and not self.has_permission():
            return HttpResponseRedirect(reverse('upgrade'))
        else:
            return super().post(request, *args, **kwargs)


    def form_valid(self, form):
        form.instance.journal_user = self.request.user
        return super(CreateToJournal, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateToJournal, self).get_context_data(**kwargs)
        context['to_journals'] = to_journal.objects.filter(journal_user=self.request.user)
        return context


class EditJournal(LoginRequiredMixin, UpdateView):
    model = to_journal
    template_name_suffix = '_update_form'
    form_class = EditJournal
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        return reverse('to-journal-entries', kwargs={'slug':self.object.slug})

    def form_valid(self, form):
        current_journal = to_journal.objects.get(journal_user=self.request.user, slug=self.kwargs['slug'])
        form.instance.journal_user = self.request.user
        form.instance.id = current_journal.id
        return super(EditJournal, self).form_valid(form)

    def get_context_data(self, **kwargs):
        current_journal = to_journal.objects.get(journal_user=self.request.user, slug=self.kwargs['slug'])
        context = super(EditJournal, self).get_context_data(**kwargs)
        context["journal_slug"] = current_journal.slug
        context["journal_id"] = current_journal.id
        return context

class DeleteJournal(LoginRequiredMixin, DeleteView):
    model = to_journal
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

class ToJournalEntriesList(LoginRequiredMixin, CreateView):
    model = to_journal_entry
    template_name = 'to_journals/to_journal_entries_list.html'
    fields = ('body', 'support_image')

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
        context["journal"] = current_journal
        context["journal_name"] = current_journal.journal_name
        context["slug"] = current_journal.slug
        context["journal_id"] = current_journal.id
        context['to_journal_entries'] = to_journal_entry.objects.filter(journal_user=self.request.user, journal_name=current_journal).order_by('-entry_date')
        return context

class EditJournalEntry(LoginRequiredMixin, UpdateView):
    model = to_journal_entry
    template_name_suffix = '_update'
    fields = ['body','support_image']
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('to-journal-entries', kwargs={'slug':self.object.journal_name.slug})

class DeleteJournalEntry(LoginRequiredMixin, DeleteView):
    model = to_journal_entry
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('to-journal-entries', kwargs={'slug':self.object.journal_name.slug})