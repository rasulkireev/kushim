from django import template
from django.forms import modelform_factory
from network.models import Contact
from network.forms import ContactForm
from network.views import CreateContact

register = template.Library()

@register.inclusion_tag('template_tags/contacts_list.html', takes_context=True)
def get_contacts(context, self):
    contacts = Contact.objects.filter(contact_owner=context['request'].user)
    return {
        'contacts': contacts,
        'form': ContactForm
        }
