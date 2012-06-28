# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models


class ChunkAdmin(admin.ModelAdmin):
    list_display = ('key', )
    search_fields = ('key', 'content')

admin.site.register(models.Chunk, ChunkAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('key', )
    search_fields = ('key', )

admin.site.register(models.Image, ImageAdmin)


class MediaAdmin(admin.ModelAdmin):
    list_display = ('key', 'title')
    search_fields = ('key', 'title', 'desc')

admin.site.register(models.Media, MediaAdmin)
