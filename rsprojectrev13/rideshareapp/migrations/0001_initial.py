# Generated by Django 5.1.1 on 2024-10-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('agency_id', models.CharField(max_length=10)),
                ('route_short_name', models.CharField(max_length=10)),
                ('route_long_name', models.CharField(max_length=100)),
                ('route_type', models.IntegerField()),
            ],
        ),
    ]
