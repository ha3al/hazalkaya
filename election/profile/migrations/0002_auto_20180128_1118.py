# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-28 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ('-created_at',), 'verbose_name': 'Kullanıcı', 'verbose_name_plural': 'Kullanıcılar'},
        ),
    ]
