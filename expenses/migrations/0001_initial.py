# Generated by Django 3.1.6 on 2021-08-07 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mode_of_payments', '0001_initial'),
        ('categories', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_incurred', models.DateField()),
                ('date_posted', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=32)),
                ('my_share', models.DecimalField(decimal_places=2, max_digits=32)),
                ('merchandise_total', models.DecimalField(decimal_places=2, max_digits=32)),
                ('merchandise_discount', models.DecimalField(decimal_places=2, default=0, max_digits=32)),
                ('shipping_fee', models.DecimalField(decimal_places=2, max_digits=32)),
                ('shipping_discount', models.DecimalField(decimal_places=2, default=0, max_digits=32)),
                ('service_fee', models.DecimalField(decimal_places=2, default=0, max_digits=32)),
                ('expected_cashback', models.DecimalField(decimal_places=2, default=0, max_digits=32)),
                ('is_pending', models.BooleanField(default=False)),
                ('is_reversal', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expense_category', to='categories.category')),
                ('mode_of_payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expense_mode_of_payment', to='mode_of_payments.modeofpayment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shared_with', models.CharField(max_length=32)),
                ('share', models.DecimalField(decimal_places=2, max_digits=32)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shared_expense', to='expenses.expense')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reversal',
            fields=[
                ('expense_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='expenses.expense')),
                ('expense', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expense_for_reversal', to='expenses.expense')),
            ],
            bases=('expenses.expense',),
        ),
        migrations.AddConstraint(
            model_name='reversal',
            constraint=models.UniqueConstraint(fields=('expense',), name='unique_expense_for_reversal'),
        ),
    ]
