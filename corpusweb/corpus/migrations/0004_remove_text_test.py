# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0003_text_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='test',
        ),
    ]
