# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_auto_20150927_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='c_details',
            name='Phone',
            field=models.CharField(max_length=10),
        ),
    ]
