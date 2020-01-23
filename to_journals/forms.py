from django.forms import ModelForm
from .models import to_journal

class EditJournal(ModelForm):

    def __init__(self, *args, **kwargs):
            super(EditJournal, self).__init__(*args, **kwargs)
            
            for fieldname in ['journal_name', 'description', 'profile_image']:
                self.fields[fieldname].help_text = None
                self.fields[fieldname].widget.attrs.update({'class':'appearance-none block mx-auto w-full bg-gray-100 text-gray-800 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'})

    class Meta:
        model = to_journal
        fields = ('journal_name', 'description', 'profile_image')
