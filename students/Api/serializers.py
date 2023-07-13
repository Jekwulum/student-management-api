from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentId', 'firstName', 'lastName', 'email', 'course', 'registrationNo']
