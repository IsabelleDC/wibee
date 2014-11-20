# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0006_auto_20141118_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
