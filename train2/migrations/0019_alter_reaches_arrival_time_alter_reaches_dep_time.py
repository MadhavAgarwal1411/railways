# Generated by Django 4.2.6 on 2023-11-26 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train2', '0018_alter_reaches_arrival_time_alter_reaches_dep_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaches',
            name='arrival_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reaches',
            name='dep_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
