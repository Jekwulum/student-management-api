# Generated by Django 4.2.3 on 2023-11-04 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('curriculumManagement', '0003_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='class_associated',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='curriculumManagement.class'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', to='teachers.teacher'),
        ),
    ]
