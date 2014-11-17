# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='creator',
            new_name='owner',
        ),
    ]
