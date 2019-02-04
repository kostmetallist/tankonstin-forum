from django import template


# for making module a valid tag library
register = template.Library()

@register.filter
def subtract(minuend, subtrahend):
    return minuend - subtrahend