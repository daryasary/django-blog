# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20150730_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('website', models.URLField(blank=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('publish', models.BooleanField()),
                ('slug', models.SlugField(blank=True)),
                ('date', models.DateField(default=datetime.datetime(2015, 7, 31, 6, 54, 14, 532871))),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('cat', models.ManyToManyField(to='blog.Category')),
                ('tag', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]
