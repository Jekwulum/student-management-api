from rest_framework.serializers import ModelSerializer
from curriculumManagement.models import Class, Subject


class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
