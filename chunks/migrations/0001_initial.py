# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(help_text='A unique name for this chunk of content', unique=True, max_length=255, verbose_name='key')),
                ('content', models.TextField(verbose_name='content', blank=True)),
            ],
            options={
                'ordering': (b'key',),
                'abstract': False,
                'verbose_name': 'Text Chunk',
                'verbose_name_plural': 'Text Chunks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(help_text='A name for chunks group', max_length=255, verbose_name='key')),
                ('content', models.TextField(verbose_name='content', blank=True)),
            ],
            options={
                'ordering': (b'key',),
                'verbose_name': 'Group Chunk',
                'verbose_name_plural': 'Group Chunks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(help_text='A unique name for this chunk of content', unique=True, max_length=255, verbose_name='key')),
                ('image', models.ImageField(upload_to='chunks/images', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': (b'key',),
                'abstract': False,
                'verbose_name': 'Image Chunk',
                'verbose_name_plural': 'Image Chunks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(help_text='A unique name for this chunk of content', unique=True, max_length=255, verbose_name='key')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('desc', models.CharField(max_length=256, null=True, verbose_name='Description', blank=True)),
                ('media', models.FileField(max_length=256, upload_to=b'chunks/media', null=True, verbose_name='Media', blank=True)),
            ],
            options={
                'ordering': (b'key',),
                'abstract': False,
                'verbose_name': 'Media Chunk',
                'verbose_name_plural': 'Media Chunks',
            },
            bases=(models.Model,),
        ),
    ]
