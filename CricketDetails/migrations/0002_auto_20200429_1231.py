# Generated by Django 2.1.5 on 2020-04-29 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CricketDetails', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batperformance',
            old_name='batting_atches',
            new_name='batting_Matches',
        ),
        migrations.RemoveField(
            model_name='batperformance',
            name='match',
        ),
        migrations.RemoveField(
            model_name='bowlperformance',
            name='match',
        ),
        migrations.AlterField(
            model_name='inning',
            name='complete_innings',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='match',
            name='full_scorecard',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='match',
            name='processing_issue',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='playerstructure',
            name='BattingStyle',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='playerstructure',
            name='BirthDate',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='playerstructure',
            name='BirthPlace',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='playerstructure',
            name='BowlingStyle',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='playerstructure',
            name='Role',
            field=models.CharField(max_length=20),
        ),
    ]
