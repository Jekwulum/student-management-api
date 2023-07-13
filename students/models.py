from django.db import models
import uuid


# Create your models here.
class Student(models.Model):
    studentId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    registrationNo = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
