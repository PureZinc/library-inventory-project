# Generated by Django 4.2 on 2024-02-03 18:45

import datetime
from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_booktracker_date_rented_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktracker',
            name='date_rented',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 18, 45, 32, 396647, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='booktracker',
            name='due_date',
            field=models.DateField(default=library.models.default_due_date),
        ),
    ]
