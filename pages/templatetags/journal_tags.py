from django import template

register = template.Library()

from to_journals.models import to_journal

@register.inclusion_tag('template_tags/journal_list.html', takes_context=True)
def get_journals(context):
  journals = to_journal.objects.filter(journal_user=context['request'].user)
  return {'journals': journals}
