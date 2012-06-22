# -*- coding: utf-8 -*-

from django import template
from django.db import models
from django.template import Context
from django.template.loader import get_template

Chunk = models.get_model('chunks', 'chunk')
Image = models.get_model('chunks', 'image')

register = template.Library()


@register.simple_tag
def chunk(key):
    return Chunk.get(key)


@register.simple_tag
def chunk_image(key):
    url = Image.objects.url(key)
    tpl = get_template('chunks/image.html')
    return tpl.render(Context(dict(url=url)))


@register.simple_tag
def chunk_imgurl(key):
    return Image.objects.url(key)
