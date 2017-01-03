# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-03 22:27
from __future__ import unicode_literals

from django.db import migrations, models

from fotopruvodce.core.text import MARKDOWN_HELP_TEXT


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0004_add_anonymous_comment_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(help_text=MARKDOWN_HELP_TEXT),
        ),
    ]
