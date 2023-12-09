# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from teachers.models import Teacher
from teachers.Api.serializers import TeacherSerializer
from users.permissions import IsStaffPermission, IsAdminPermission
from users.Api.serializers import CustomUserSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class TeacherListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStaffPermission]

    def get(self, request: Request):
        teachers = Teacher.objects.all()
        print(teachers)
        serializer = TeacherSerializer(teachers, many=True)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Teachers records retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    def post(self, request: Request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"message": "Teacher record created successfully", "status": "SUCCESS", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(data={"message": serializer.errors, "status": "FAILED"}, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailView(APIView):
    def get_object(self, pk=None):
        try:
            teacher = Teacher.objects.get(teacher_id=pk)
            return teacher
        except Teacher.DoesNotExist:
            return None

    def get(self, request: Request, pk=None):
        teacher = self.get_object(pk)
        if teacher is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Teacher record not found", "status": "FAILED"})

        serializer = TeacherSerializer(teacher)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Teacher's record retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    def patch(self, request: Request, pk=None):
        teacher = self.get_object(pk)
        if teacher is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Teacher record not found", "status": "FAILED"})
        serializer = TeacherSerializer(
            instance=teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK,
                            data={"message": "Teacher's record updated",
                                  "data": serializer.data,
                                  "status": "SUCCESS"})
        return Response(data={"message": serializer.errors, "status": "FAILED"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk=None):
        teacher = self.get_object(pk)
        if teacher is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Teacher record not found", "status": "FAILED"})

        teacher.delete()
        user = User.objects.get(user_id=teacher.user.user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={"message": "Teacher's record deleted", "status": "SUCCESS"})
