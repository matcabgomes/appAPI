# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dadospessoais',
            options={'verbose_name': 'Dados Pessoais', 'verbose_name_plural': 'Dados Pessoais'},
        ),
    ]