# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_exim', '0010_merge_20170614_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsource',
            name='crm_type',
            field=models.CharField(choices=[('actionkit_api', 'actionkit_api'), ('facebook', 'facebook')], max_length=16),
        ),
        migrations.AlterField(
            model_name='eventsource',
            name='update_style',
            field=models.IntegerField(choices=[(0, 'manual or ping only'), (3, 'daily pull'), (4, 'hourly pull')]),
        ),
    ]