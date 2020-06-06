# Generated by Django 2.1.5 on 2020-04-30 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CricketDetails', '0015_auto_20200430_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='Team1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='teamA', to='CricketDetails.TeamStructure'),
        ),
        migrations.AddField(
            model_name='score',
            name='Team2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='teamB', to='CricketDetails.TeamStructure'),
        ),
    ]