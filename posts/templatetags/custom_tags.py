from django import template
from posts.models import *

register = template.Library()

@register.simple_tag(name="categories")
def all_catagories():
    return Category.objects.all()


@register.simple_tag(name="tags")
def all_tags():
    return Tag.objects.all()