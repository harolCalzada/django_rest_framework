# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-24 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='languaje',
            new_name='language',
        ),
    ]
