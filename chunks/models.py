# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _
from django.template.base import Lexer
from . import managers

CACHE_PREFIX = 'chunks_'


class BaseChunk(models.Model):

    key = models.CharField(_(u'key'), max_length=255, unique=True,
                           help_text=_(u'A unique name for this chunk of content'))

    class Meta:
        abstract = True
        ordering = ('key', )

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

    class Meta(BaseChunk.Meta):
        verbose_name = _(u'Text Chunk')
        verbose_name_plural = _(u'Text Chunks')

    def save(self, *args, **kwargs):
        cache.delete(CACHE_PREFIX + get_language() + self.key)  # cache invalidation on save
        super(Chunk, self).save(*args, **kwargs)

    @staticmethod
    def process_token(token):
        #process TOKEN_VAR only
        if token.token_type == 1:
            return Chunk.get(token.contents)
        else:
            return token.contents    

    @staticmethod
    def get(key):
        cache_key = CACHE_PREFIX + 'image' + get_language() + key
        content = cache.get(cache_key)
        if content is None:
            obj, created = Chunk.objects.get_or_create(
                key=key, defaults={'content': key})
            #a content can to contain other chunks as vars
            lexer = Lexer(obj.content,0)
            content = ''.join(map(Chunk.process_token,lexer.tokenize()))
            cache.set(cache_key, content)
        return content


class Image(BaseChunk):
    u"""
    The same thing like Chunk but for images.
    """
    image = models.ImageField(_(u'image'), upload_to=u'chunks/images', max_length=255)

    objects = managers.ImageManager()

    class Meta(BaseChunk.Meta):
        verbose_name = _(u'Image Chunk')
        verbose_name_plural = _(u'Image Chunks')


class Media(BaseChunk):
    u"""
    The same thing like Chunk but for files.
    """
    title = models.CharField(max_length=64, verbose_name=_(u'Title'))
    desc = models.CharField(max_length=256, blank=True, null=True, verbose_name=_(u'Description'))
    media = models.FileField(upload_to='chunks/media', max_length=256, blank=True, null=True, verbose_name=_(u'Media'))

    class Meta(BaseChunk.Meta):
        verbose_name = _(u'Media Chunk')
        verbose_name_plural = _(u'Media Chunks')

    @staticmethod
    def get(key):
        cache_key = CACHE_PREFIX + 'media' + get_language() + key
        obj = cache.get(cache_key)
        if obj is None:
            obj, created = Media.objects.get_or_create(
                key=key, defaults={'title': key})
            cache.set(cache_key, obj)
        return obj
