# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 21:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(720)])),
                ('message', models.CharField(max_length=140)),
            ],
        ),
    ]
