from django.forms import ModelForm
from .models import Contact, ContactContact

class EditContact(ModelForm):

    def __init__(self, *args, **kwargs):
            super(EditContact, self).__init__(*args, **kwargs)
            
            for fieldname in ['first_name', 'last_name', 'tags', 'how_you_met', 'current_location', 'date_of_birth', 'title', 'employer']:
                self.fields[fieldname].help_text = None
                self.fields[fieldname].widget.attrs.update({'class':'appearance-none block mx-auto w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'})
                
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'profile_image', 'tags', 'how_you_met', 'current_location', 'date_of_birth', 'title', 'employer')


class ContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)

            for fieldname in ['first_name', 'last_name']:
                self.fields[fieldname].help_text = None
                self.fields[fieldname].widget.attrs.update({'class':'homepage-add-contact'})

            for fieldname in ['first_name']:
                self.fields[fieldname].widget.attrs.update({'placeholder':'First Name'})

            for fieldname in ['last_name']:
                self.fields[fieldname].widget.attrs.update({'placeholder':'Last Name'})
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name')


class ContactContactForm(ModelForm):

    def __init__(self, *args, **kwargs):
            super(ContactContactForm, self).__init__(*args, **kwargs)

            for fieldname in ['contact_type', 'contact_value']:
                self.fields[fieldname].help_text = None
                self.fields[fieldname].widget.attrs.update({'class':'homepage-add-contact'})

            for fieldname in ['contact_type']:
                self.fields[fieldname].widget.attrs.update({'placeholder':'Type'})

            for fieldname in ['contact_value']:
                self.fields[fieldname].widget.attrs.update({'placeholder':'Value'})
    class Meta:
        model = ContactContact
        fields = ('contact_type', 'contact_value')