import datetime
from django import template
from posts.models import Post

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def num_drafts():
    return Post.objects.get_queryset().filter(published_at__isnull=True).count()