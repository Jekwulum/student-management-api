from django.db import models
import uuid
from teachers.models import Teacher
from students.models import Student


# Create your models here.
class Class(models.Model):
    class_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return self.name

class Subject(models.Model):
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    teachers = models.ManyToManyField(Teacher, related_name='teachers')
    class_associated = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.name

class Result(models.Model):
    result_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.date}"
