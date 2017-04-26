# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-25 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20170425_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=55)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board')),
            ],
        ),
    ]
