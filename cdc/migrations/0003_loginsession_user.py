# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdc', '0002_loginsession'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginsession',
            name='user',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
