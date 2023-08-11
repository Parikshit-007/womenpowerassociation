from django import template

register = template.Library()

@register.filter
def custom_slice(lst, index):
    return lst[index:index+4]
