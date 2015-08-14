# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20150814_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 8, 14, 8, 34, 35, 216406)),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=redactor.fields.RedactorField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 14, 8, 34, 35, 209678)),
        ),
    ]
