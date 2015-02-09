# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdc', '0003_loginsession_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(default=b'', max_length=1000)),
                ('postedby', models.CharField(default=b'', max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
