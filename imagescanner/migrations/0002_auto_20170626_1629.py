# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagescanner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='email_address',
            field=models.CharField(default=b'example@gmail.com', max_length=700),
        ),
        migrations.AddField(
            model_name='upload',
            name='first_name',
            field=models.CharField(default=b'John', max_length=500),
        ),
        migrations.AddField(
            model_name='upload',
            name='last_name',
            field=models.CharField(default=b'smith', max_length=200),
        ),
        migrations.AlterField(
            model_name='upload',
            name='file_name',
            field=models.CharField(default=b'resume', max_length=300),
        ),
    ]
