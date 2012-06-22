# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache
from django.utils.translation import ugettext_lazy as _

from . import managers

CACHE_PREFIX = 'chunks_'


class BaseChunk(models.Model):

    key = models.CharField(_(u'key'), max_length=255, unique=True,
                           help_text=_(u'A unique name for this chunk of content'))

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.key


class Chunk(BaseChunk):
    u"""
    A Chunk is a piece of content associated
    with a unique key that can be inserted into
    any template with the use of a special template
    tag
    """
    content = models.TextField(_(u'content'), blank=True)

    class Meta:
        verbose_name = _(u'Text Chunk')
        verbose_name_plural = _(u'Text Chunks')

    def save(self, *args, **kwargs):
        cache.delete(CACHE_PREFIX + self.key)  # cache invalidation on save
        super(Chunk, self).save(*args, **kwargs)

    @staticmethod
    def get(key):
        cache_key = CACHE_PREFIX + key
        content = cache.get(cache_key)
        if content is None:
            obj, c_ = Chunk.objects.get_or_create(key=key, defaults={'content': key})
            cache.set(cache_key, obj.content)
            content = obj.content
        else:
            content += '(from cache)'
        return content


class Image(BaseChunk):
    u"""
    The same thing like Chunk but for images.
    """
    image = models.ImageField(_(u'image'), upload_to=u'chunks', max_length=255)

    objects = managers.ImageManager()

    class Meta:
        verbose_name = _(u'Image Chunk')
        verbose_name_plural = _(u'Image Chunks')
