# Generated by Django 3.2.5 on 2021-08-05 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('mode_of_payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeofpayment',
            name='cut_off',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='days_in_a_year',
            field=models.PositiveIntegerField(choices=[(365, '365'), (365, '360')], null=True),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='frequency_of_interest_computation',
            field=models.CharField(choices=[(1, 1), (7, 7), (14, 14), (30, 30), (90, 90)], max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='frequency_of_interest_crediting',
            field=models.CharField(choices=[(1, 1), (7, 7), (14, 14), (30, 30), (90, 90)], max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='interest_credited_at',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='interest_rate_per_annum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=32),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='login_url',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='minimum_maintaining_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=32),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.user'),
        ),
        migrations.AddField(
            model_name='modeofpayment',
            name='website',
            field=models.URLField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='modeofpayment',
            name='starting_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=32),
        ),
    ]
