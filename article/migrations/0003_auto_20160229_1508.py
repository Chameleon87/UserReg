# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160229_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
