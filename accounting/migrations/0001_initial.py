# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('CustID', models.AutoField(serialize=False, primary_key=True)),
                ('CustName', models.CharField(max_length=200)),
                ('AddStreet', models.CharField(max_length=200)),
                ('AddDistrict', models.CharField(max_length=200)),
                ('AddState', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField()),
                ('PendingAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('ManaID', models.AutoField(serialize=False, primary_key=True)),
                ('ManaName', models.CharField(max_length=200)),
                ('ManaAuth', models.CharField(default=b'Normal', max_length=10)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
