# Generated by Django 2.1.5 on 2020-04-30 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CricketDetails', '0008_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]