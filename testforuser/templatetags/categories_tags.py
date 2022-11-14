from django import template

from testforuser.models import Category


register = template.Library()
@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_int(t):
    try:
        return int(t)
    except ValueError:
        return 0
