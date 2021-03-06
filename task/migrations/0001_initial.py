# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('a', models.CharField(blank=True, default=None, max_length=16)),
                ('b', models.CharField(blank=True, default=None, max_length=16)),
            ],
            options={
                'verbose_name': 'Набор данных',
                'verbose_name_plural': 'Наборы данных',
            },
        ),
        migrations.CreateModel(
            name='Exception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default=None, max_length=68)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Data')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, default=None, max_length=13)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Data')),
            ],
        ),
    ]
