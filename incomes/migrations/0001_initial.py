# Generated by Django 3.1.6 on 2021-08-07 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mode_of_payments', '0001_initial'),
        ('users', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_incurred', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=32)),
                ('details', models.TextField(null=True)),
                ('mode_of_payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='income_mode_of_payment', to='mode_of_payments.modeofpayment')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='source_of_income', to='categories.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
