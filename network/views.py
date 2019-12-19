from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Contact, ContactLog, ContactContact
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .forms import EditContact, ContactForm, ContactContactForm

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
    form_class = EditContact
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        return reverse('contact-detail', kwargs={'id':self.kwargs['id']})

    def form_valid(self, form):
        current_contact = Contact.objects.get(contact_owner=self.request.user, contact_id=self.kwargs['contact_id'])
        form.instance.contact_owner = self.request.user
        form.instance.contact_id = current_contact.contact_id
        return super(EditContact, self).form_valid(form)

class CreateContactContact(LoginRequiredMixin, CreateView):
    model = ContactContact
    template_name = 'network/contact_contacts.html'
    fields = ('contact_type','contact_value',)

    def get_success_url(self):
        return reverse('contact-detail', kwargs={'id':self.kwargs['id']})

    def form_valid(self, form):
        current_contact = Contact.objects.get(contact_owner=self.request.user, contact_id=self.kwargs['contact_id'])
        form.instance.contact_owner = self.request.user
        form.instance.contact_id = current_contact
        return super(CreateContactContact, self).form_valid(form)

    def get_context_data(self, **kwargs):
        current_contact = Contact.objects.get(contact_owner=self.request.user, contact_id=self.kwargs['contact_id'])
        context = super(CreateContactContact, self).get_context_data(**kwargs)
        context["contact_info"] = current_contact
        context["first_name"] = current_contact.first_name
        context["id"] = current_contact.contact_id
        context['contact_contacts'] = ContactContact.objects.filter(contact_owner=self.request.user, contact_id=current_contact)
        return context


class CreateContactLog(LoginRequiredMixin, CreateView):
    model = ContactLog
    template_name = 'network/contact_detail.html'
    fields = ('log_type','body',)

    def get_success_url(self):
        return reverse('contact-detail', kwargs={'contact_id':self.object.contact_id.contact_id})

    def form_valid(self, form):
        current_contact = Contact.objects.get(contact_owner=self.request.user, contact_id=self.kwargs['contact_id'])
        form.instance.contact_owner = self.request.user
        form.instance.contact_id = current_contact
        return super(CreateContactLog, self).form_valid(form)

    def get_context_data(self, **kwargs):
        current_contact = Contact.objects.get(contact_owner=self.request.user, contact_id=self.kwargs['contact_id'])
        context = super(CreateContactLog, self).get_context_data(**kwargs)
        context["contact_info"] = current_contact
        context["first_name"] = current_contact.first_name
        context["id"] = current_contact.contact_id
        context['log_entries'] = ContactLog.objects.filter(contact_owner=self.request.user, contact_id=current_contact)
        context['contact_contacts'] = ContactContact.objects.filter(contact_owner=self.request.user, contact_id=current_contact)
        context['contacts_form'] = ContactContactForm()
        return context

class EditContactLog(LoginRequiredMixin, UpdateView):
    model = ContactLog
    template_name_suffix = '_update'
    fields = ['log_type','body']
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('contact-detail', kwargs={'contact_id':self.object.contact_id.contact_id})

class DeleteContactLog(LoginRequiredMixin, DeleteView):
    model = ContactLog
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('contact-detail', kwargs={'contact_id':self.object.contact_id.contact_id})