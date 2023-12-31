from rest_framework.serializers import ModelSerializer
from curriculumManagement.models import Class, Subject, Result, Attendance


class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class AttendanceSerializer(ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
