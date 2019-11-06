from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Contact, ContactForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import render



class CreateContact(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'network/contacts_list.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.contact_owner = self.request.user
        return super(CreateContact, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateContact, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.filter(contact_owner=self.request.user)
        return context
