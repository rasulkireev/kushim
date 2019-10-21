from django import template
from django.forms import modelform_factory
from to_journals.models import to_journal
from to_journals.views import CreateToJournal

register = template.Library()

@register.inclusion_tag('template_tags/journal_list.html', takes_context=True)
def get_journals(context, self):
    journals = to_journal.objects.filter(journal_user=context['request'].user)
    return {'journals': journals}
