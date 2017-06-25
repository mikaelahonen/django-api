import bleach
import json as jsonlib

from django import template

from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def json(value):
    """safe jsonify filter, bleaches the json string using the bleach html tag remover"""
    uncleaned = jsonlib.dumps(value)
    clean = bleach.clean(uncleaned)
    return mark_safe(clean)