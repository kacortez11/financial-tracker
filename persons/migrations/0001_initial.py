# Generated by Django 3.1.6 on 2021-09-18 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=16)),
                ('display_name', models.CharField(max_length=16, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]