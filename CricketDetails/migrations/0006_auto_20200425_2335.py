# Generated by Django 2.1.5 on 2020-04-25 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CricketDetails', '0005_auto_20200425_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamstructure',
            name='logo1',
            field=models.ImageField(upload_to='images/', verbose_name='logo1'),
        ),
        migrations.AlterField(
            model_name='teamstructure',
            name='logo2',
            field=models.ImageField(upload_to='images/', verbose_name='logo2'),
        ),
        migrations.AlterField(
            model_name='teamstructure',
            name='logo3',
            field=models.ImageField(upload_to='images/', verbose_name='logo3'),
        ),
    ]