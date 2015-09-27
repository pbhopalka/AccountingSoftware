# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20150927_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill_Record',
            fields=[
                ('BillID', models.AutoField(serialize=False, primary_key=True)),
                ('Date', models.DateField()),
                ('Amount', models.IntegerField(default=0)),
                ('Cust_ID', models.ForeignKey(to='accounting.C_Details')),
            ],
        ),
    ]
