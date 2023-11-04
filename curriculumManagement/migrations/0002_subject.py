# Generated by Django 4.2.3 on 2023-11-04 16:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('curriculumManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('class_associated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='curriculumManagement.class')),
                ('teachers', models.ManyToManyField(related_name='subjects', to='teachers.teacher')),
            ],
        ),
    ]
