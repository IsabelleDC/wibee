# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0003_auto_20141116_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=b'categories', blank=True),
            preserve_default=True,
        ),
    ]
