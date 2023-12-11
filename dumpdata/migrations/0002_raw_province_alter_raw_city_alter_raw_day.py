# Generated by Django 5.0 on 2023-12-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dumpdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raw',
            name='province',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='raw',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='raw',
            name='day',
            field=models.DateTimeField(),
        ),
    ]