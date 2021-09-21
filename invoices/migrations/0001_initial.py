# Generated by Django 3.1.6 on 2021-09-21 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=32)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=32)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=32)),
                ('bill_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='person_to_invoice', to='users.person')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
