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

class EditContact(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name_suffix = '_update_form'
    pk_url_kwarg = 'id'
    fields = ('first_name', 'last_name', 'nickname', 'profile_image', 'tags', 'how_you_met', 'current_location', 'date_of_birth', 'title', 'employer')
    
    def get_success_url(self):
        return reverse('contact-detail', kwargs={'id':self.kwargs['id']})

    def form_valid(self, form):
        current_contact = Contact.objects.get(contact_owner=self.request.user, contact_id=self.kwargs['id'])
        form.instance.contact_owner = self.request.user
        form.instance.contact_id = current_contact.contact_id
        return super(EditContact, self).form_valid(form)



class CreateContactLog(LoginRequiredMixin, CreateView):
    model = ContactLog
    template_name = 'network/contact_detail.html'
    fields = ('log_type','body',)

    def get_success_url(self):
        return reverse('contact-detail', kwargs={'id':self.kwargs['id']})

    def form_valid(self, form):
        current_contact = Contact.objects.get(contact_owner=self.request.user, contact_id=self.kwargs['id'])
        form.instance.contact_owner = self.request.user
        form.instance.contact_id = current_contact
        return super(CreateContactLog, self).form_valid(form)

    def get_context_data(self, **kwargs):
        current_contact = Contact.objects.get(contact_owner=self.request.user, contact_id=self.kwargs['id'])
        context = super(CreateContactLog, self).get_context_data(**kwargs)
        context["contact_info"] = current_contact
        context["first_name"] = current_contact.first_name
        context["id"] = current_contact.contact_id
        context['log_entries'] = ContactLog.objects.filter(contact_owner=self.request.user, contact_id=current_contact)
        return context
