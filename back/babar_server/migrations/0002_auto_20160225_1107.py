# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 11:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('babar_server', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='money',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='money',
            new_name='amount',
        ),
    ]
