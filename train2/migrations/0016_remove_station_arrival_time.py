# Generated by Django 4.2.6 on 2023-11-25 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train2', '0015_train_arrival_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='arrival_time',
        ),
    ]
