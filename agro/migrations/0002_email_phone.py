# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='phone',
            field=models.CharField(db_index=True, default=0, max_length=200),
            preserve_default=False,
        ),
    ]
