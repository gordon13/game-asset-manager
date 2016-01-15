# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='asset_location',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='notes',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[(b'open', b'open'), (b'in_progress', b'In progress'), (b'done', b'Done'), (b'to_be_deleted', b'To be deleted')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[(b'art', b'Art'), (b'audio', b'Audio'), (b'writing', b'Writing')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
