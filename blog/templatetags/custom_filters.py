from django import template
from django.utils.timesince import timesince as timesince_
from datetime import datetime

register = template.Library()

@register.filter
def custom_timesince(value):
    if value.days == 0 and value.seconds < 3600:  # Less than 1 hour
        minutes = value.seconds // 60
        return f"{minutes} {'minute' if minutes == 1 else 'minutes'}"
    else:
        return value
