# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-22 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ON', 'On'), ('OFF', 'Off')], default='OFF', max_length=5)),
            ],
        ),
    ]
