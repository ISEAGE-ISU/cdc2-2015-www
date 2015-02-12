# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdc', '0004_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='email',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='text',
            field=models.TextField(default=b'', max_length=1000),
            preserve_default=True,
        ),
    ]
