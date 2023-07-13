# Generated by Django 4.2.3 on 2023-07-13 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.UUIDField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('registrationNo', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
    ]