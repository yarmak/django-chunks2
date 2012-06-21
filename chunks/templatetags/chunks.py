# -*- coding: utf-8 -*-

from django import template
from django.db import models

Chunk = models.get_model('chunks', 'chunk')

register = template.Library()


@register.simple_tag
def chunk(key):
    return Chunk.get(key)
