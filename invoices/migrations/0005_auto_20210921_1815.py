# Generated by Django 3.1.6 on 2021-09-21 18:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_auto_20210921_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 21, 18, 15, 11, 329827, tzinfo=utc)),
        ),
    ]