# Generated by Django 4.2 on 2024-02-02 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_booktracker_date_rented_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktracker',
            name='date_rented',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 2, 14, 45, 31, 19925, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='booktracker',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 2, 14, 45, 31, 19925, tzinfo=datetime.timezone.utc)),
        ),
    ]
