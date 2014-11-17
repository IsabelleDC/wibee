# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0002_auto_20141115_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='state',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='zip_code',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='country',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(null=True, upload_to=b'places', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
