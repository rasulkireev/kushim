from django.forms import ModelForm
from .models import Contact, ContactContact

class EditContact(ModelForm):

    def __init__(self, *args, **kwargs):
            super(EditContact, self).__init__(*args, **kwargs)
            
            for fieldname in ['first_name', 'last_name', 'tags', 'description', 'profile_image','how_you_met', 'contact_frequency','current_location', 'date_of_birth', 'title', 'employer']:
                self.fields[fieldname].help_text = None
                self.fields[fieldname].widget.attrs.update({'class':'appearance-none block mx-auto w-full bg-gray-100 text-gray-800 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'})
                
            for fieldname in ['date_of_birth']:
                self.fields[fieldname].widget.attrs.update({'placeholder':'mm/dd/yyyy'})

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'profile_image', 'tags', 'description', 'contact_frequency', 'how_you_met', 'current_location', 'date_of_birth', 'title', 'employer')

        def clean_photo(self):
            data = self.cleaned_data.get("profile_image")
            if data is False:
                data = None
            return data



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
                self.fields[fieldname].widget.attrs.update({'class':'block appearance-none w-full bg-white border border-grey-light hover:border-grey px-2 py-2 rounded shadow'})

            for fieldname in ['contact_type']:
                self.fields[fieldname].widget.attrs.update({'placeholder':'Email'})

            for fieldname in ['contact_value']:
                self.fields[fieldname].widget.attrs.update({'placeholder':'someone@example.com'})
    class Meta:
        model = ContactContact
        fields = ('contact_type', 'contact_value')