# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header',
            field=models.ImageField(blank=True, null=True, upload_to=b'headers/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='lang',
            field=models.CharField(choices=[(b'fa', 'Farsi'), (b'en', 'English')], default=b'En-us', max_length=8, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]