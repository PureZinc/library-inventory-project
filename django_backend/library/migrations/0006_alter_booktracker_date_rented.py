# Generated by Django 4.2 on 2024-02-09 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_booktracker_date_rented_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktracker',
            name='date_rented',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 9, 19, 0, 4, 312221, tzinfo=datetime.timezone.utc)),
        ),
    ]