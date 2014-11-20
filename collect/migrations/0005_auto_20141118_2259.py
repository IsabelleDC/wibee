# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0004_auto_20141117_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=7, choices=[(b'Restaurant', b'Restaurant'), (b'Hotel', b'Hotel'), (b'View', b'View'), (b'Shop', b'Shop')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='state',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='zip_code',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
