# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_auto_20150927_2213'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerDetails',
            new_name='C_Details',
        ),
    ]
