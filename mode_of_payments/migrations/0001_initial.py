# Generated by Django 3.1.6 on 2021-08-07 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
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
                ('is_active', models.BooleanField(default=True)),
                ('date_deactivated', models.DateField(null=True)),
                ('priority', models.PositiveIntegerField(default=99)),
                ('default', models.BooleanField(default=False)),
                ('currency', models.CharField(default='PHP', max_length=4)),
                ('starting_balance', models.DecimalField(decimal_places=2, default=0, max_digits=32)),
                ('interest_rate_per_annum', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('interest_credited_at', models.PositiveSmallIntegerField(default=1)),
                ('frequency_of_interest_computation', models.CharField(choices=[(1, 'Daily'), (7, 'Weekly'), (14, 'Every two weeks'), (30, 'Monthly'), (90, 'Quarterly')], max_length=16, null=True)),
                ('frequency_of_interest_crediting', models.CharField(choices=[(1, 'Daily'), (7, 'Weekly'), (14, 'Every two weeks'), (30, 'Monthly'), (90, 'Quarterly')], max_length=16, null=True)),
                ('days_in_a_year', models.PositiveSmallIntegerField(choices=[(365, '365'), (365, '360')], null=True)),
                ('minimum_maintaining_balance', models.DecimalField(decimal_places=2, default=0, max_digits=32)),
                ('cut_off', models.PositiveSmallIntegerField(null=True)),
                ('branch', models.CharField(max_length=64, null=True)),
                ('account_number', models.CharField(max_length=32, null=True)),
                ('website', models.URLField(max_length=256, null=True)),
                ('login_url', models.CharField(max_length=32, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
