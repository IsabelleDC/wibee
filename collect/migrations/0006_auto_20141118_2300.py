# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0005_auto_20141118_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=15, choices=[(b'Restaurant', b'Restaurant'), (b'Hotel', b'Hotel'), (b'View', b'View'), (b'Shop', b'Shop')]),
            preserve_default=True,
        ),
    ]
