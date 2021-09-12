# Generated by Django 3.1.6 on 2021-09-12 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20210912_0853'),
        ('incomes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='payment_invoice', to='invoices.invoice'),
        ),
    ]
