from django.utils import timezone
from django import template


register = template.Library()


@register.filter
def get_date_string(value):
    # {{ book.date_added | get_date_string }}
    now = timezone.now()
    delta = now - value

    if delta.days == 0:
        return 'Today'
    if delta.days == 1:
        return 'Yesterday'
    if delta.days > 1:
        return f'{abs(delta.days)} {"day" if abs(delta.days) == 1 else "days"} ago'