# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0005_bill_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Record',
            fields=[
                ('PaymentID', models.AutoField(serialize=False, primary_key=True)),
                ('Date', models.DateField()),
                ('Amount', models.IntegerField(default=0)),
                ('Cust_ID', models.ForeignKey(to='accounting.C_Details')),
            ],
        ),
        migrations.AlterField(
            model_name='manager',
            name='ManaAuth',
            field=models.CharField(default=b'normal', max_length=10),
        ),
    ]
