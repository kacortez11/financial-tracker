# Generated by Django 3.2.5 on 2021-08-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModeOfPayment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=32)),
                ('label', models.CharField(max_length=32)),
                ('type', models.CharField(choices=[('cash', 'Cash'), ('traditional_bank', 'Bank'), ('digital_bank', 'Digital'), ('e_wallet', 'E-wallet'), ('in_app_wallet', 'App Integrated Wallet')], max_length=32)),
                ('debit', models.BooleanField(default=True)),
                ('credit', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('starting_balance', models.FloatField(default=0)),
                ('currency', models.CharField(default='PHP', max_length=4)),
                ('branch', models.CharField(max_length=64, null=True)),
                ('account_number', models.CharField(max_length=32, null=True)),
                ('date_deactivated', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
