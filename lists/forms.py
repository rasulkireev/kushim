from django.forms import ModelForm
from .models import List

class EditGarden(ModelForm):

    def __init__(self, *args, **kwargs):
            super(EditGarden, self).__init__(*args, **kwargs)
            
            for fieldname in ['list_name', 'description', 'profile_image']:
                self.fields[fieldname].help_text = None
                self.fields[fieldname].widget.attrs.update({'class':'appearance-none block mx-auto w-full bg-gray-100 text-gray-800 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'})

    class Meta:
        model = List
        fields = ('list_name', 'description', 'profile_image')

        def clean_photo(self):
            data = self.cleaned_data.get("profile_image")
            if data is False:
                data = None
            return data