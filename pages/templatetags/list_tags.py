from django import template
from django.forms import modelform_factory
from lists.models import List, ListForm
from lists.views import CreateList

register = template.Library()

@register.inclusion_tag('template_tags/list_list.html', takes_context=True)
def get_lists(context, self):
    lists = List.objects.filter(list_owner=context['request'].user)
    return {
        'lists': lists,
        'form': ListForm
        }
