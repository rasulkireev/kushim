from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import List, ListEntry, ListForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import render



class CreateList(LoginRequiredMixin, CreateView):
    model = List
    template_name = 'lists/lists_list.html'
    form_class = ListForm

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.list_owner = self.request.user
        return super(CreateList, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateList, self).get_context_data(**kwargs)
        context['lists'] = List.objects.filter(list_owner=self.request.user)
        return context


class DeleteList(LoginRequiredMixin, DeleteView):
    model = List
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

class RenameList(LoginRequiredMixin, UpdateView):
    model = List
    template_name_suffix = '_update_form'
    fields = ['list_name']
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'



class CreateListEntry(LoginRequiredMixin, CreateView):
    model = ListEntry
    template_name = 'lists/list_entries_list.html'
    fields = ('body',)

    def get_success_url(self):
        return reverse('list-entries', kwargs={'slug':self.object.list_name.slug})

    def form_valid(self, form):
        current_list = List.objects.get(list_owner=self.request.user, slug=self.kwargs['slug'])
        form.instance.list_owner = self.request.user
        form.instance.list_name = current_list
        return super(CreateListEntry, self).form_valid(form)

    def get_context_data(self, **kwargs):
        current_list = List.objects.get(list_owner=self.request.user, slug=self.kwargs['slug'])
        context = super(CreateListEntry, self).get_context_data(**kwargs)
        context["list_name"] = current_list.list_name
        context["slug"] = current_list.slug
        context['list_entries'] = ListEntry.objects.filter(list_owner=self.request.user, list_name=current_list).order_by('-entry_date')
        return context

class EditListEntry(LoginRequiredMixin, UpdateView):
    model = ListEntry
    template_name_suffix = '_update'
    fields = ['body']
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('list-entries', kwargs={'slug':self.object.list_name.slug})
