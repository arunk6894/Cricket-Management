# Generated by Django 2.1.5 on 2020-04-30 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CricketDetails', '0010_auto_20200430_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='Toss_won_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tosswon', to='CricketDetails.TeamStructure'),
        ),
    ]
