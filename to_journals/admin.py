from django.contrib import admin
from .models import to_journal, to_journal_entry




admin.site.register(to_journal)
admin.site.register(to_journal_entry)
