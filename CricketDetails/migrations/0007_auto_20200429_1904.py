# Generated by Django 2.1.5 on 2020-04-29 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CricketDetails', '0006_auto_20200429_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
