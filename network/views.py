from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Contact, ContactForm, ContactLog
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

class CreateLog(LoginRequiredMixin, CreateView):
    model = ContactLog
    template_name = 'network/contact_detail.html'
    fields = ('log_type','body',)

    def get_success_url(self):
        return reverse('contact-detail', kwargs={'pk':self.object.contact_id})

    def form_valid(self, form):
        current_contact = Contact.objects.get(contact_owner=self.request.user, contact_id=self.contact_id)
        form.instance.contact_owner = self.request.user
        form.instance.contact_id = current_contact
        return super(CreateLog, self).form_valid(form)

    def get_context_data(self, **kwargs):
        current_contact = Contact.objects.get(contact_owner=self.request.user, contact_id=self.contact_id)
        context = super(CreateLog, self).get_context_data(**kwargs)
        context["contact-info"] = current_contact
        context["id"] = current_contact.contact_id
        context['log-entries'] = ContactLog.objects.filter(contact_owner=self.request.user, contact_id=current_contact)
        return context
