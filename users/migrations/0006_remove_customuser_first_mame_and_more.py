# Generated by Django 4.2.3 on 2023-07-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_first_mame_alter_customuser_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_mame',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
    ]
