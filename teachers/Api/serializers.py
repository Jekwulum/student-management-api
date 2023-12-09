from rest_framework import serializers
from teachers.models import Teacher
from users.Api.serializers import CustomUserSerializer

class TeacherSerializer(serializers.ModelSerializer):
    # user = CustomUserSerializer(required=False, read_only=True)
    class Meta:
        model = Teacher
        fields = '__all__'

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user', None)  # Remove 'user' from validated_data
    #     teacher = Teacher.objects.create(**validated_data)

    #     if user_data:
    #         # user = CustomUser.objects.create(**user_data)
    #         user_serializer = CustomUserSerializer(data=user_data)
    #         user_serializer.is_valid(raise_exception=True)
    #         user_serializer.save()
    #         print(user_serializer.data)
    #         teacher.user = user_serializer.data.user_id
    #         teacher.save()

    #     return teacher
