from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class Teacher(models.Model):
    teacher_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
