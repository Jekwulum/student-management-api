import random
import datetime
from django.db import IntegrityError, transaction
from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from students.models import Student
from .serializers import StudentSerializer
from users.Api.serializers import CustomUserSerializer
from users.permissions import IsStaffPermission, IsAdminPermission

from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['GET'])
def student_search(request: Request, pk=None):
    """
    :param request:
    :param pk: pk could be the email or registrationNo of the record being searched for
    :return:
    This endpoint returns a student's record by searching by either email or registrationNo
    """
    try:
        student = Student.objects.get(Q(email=pk) | Q(registrationNo=pk))
        serializer = StudentSerializer(student)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Student's record retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={"message": "student record not found", "status": "FAILED"})


class StudentListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStaffPermission]

    def get(self, request: Request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Students records retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    @transaction.atomic
    def post(self, request: Request):
        user_data = request.data.pop("user")
        student_data = request.data
        confirm_password = user_data.pop("confirm_password")

        if user_data["password"] != confirm_password:
            return Response({"message": 'Passwords do not match!', "status": "FAILED"},
                            status=status.HTTP_400_BAD_REQUEST)

        custom_user_serializer = CustomUserSerializer(data=user_data)

        if custom_user_serializer.is_valid(raise_exception=True):
            user = None
            try:
                with transaction.atomic():
                    user = custom_user_serializer.save()
                    number = random.randint(0, 9999)

                    student = Student.objects.create(
                        user=user,
                        registration_num=f"{datetime.date.today().year}-STU-{number:04}",
                        course=student_data["course"]
                    )
                    student.save()
                    return Response({"message": "Student created successfully", "status": "SUCCESS"},
                                    status=status.HTTP_201_CREATED)
            except (IntegrityError, ValidationError) as e:
                if user:
                    user.delete()
                return Response({"message": 'Invalid data provided for student creation.', "status": "FAILED"},
                                status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                print("error ", e)
                if user:
                    user.delete()
                return Response({"message": 'An error occurred during student creation.', "status": "FAILED"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": custom_user_serializer.errors, "status": "FAILED"},
                        status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStaffPermission]

    # def delete_permissions(self):
    #     # Customize permissions for GET method
    #     if self.request.method == 'GET':
    #         return [IsStaffPermission()]
    #     # Default permissions for other methods
    #     return super().get_permissions()
    #
    # def delete_permissions(self):
    #     if self.request.method == 'DELETE':
    #         return [IsAdminPermission()]
    #     # Default permissions for other methods
    #     return super().delete_permissions()

    def get_object(self, pk=None):
        print(pk)
        try:
            student = Student.objects.get(student_id=pk)
            return student
        except Student.DoesNotExist:
            return None

    def get(self, request: Request, pk=None):
        student = self.get_object(pk)
        if student is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "student record not found", "status": "FAILED"})

        serializer = StudentSerializer(student)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Student's record retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    def patch(self, request: Request, pk=None):
        student = self.get_object(pk)
        if student is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "student's record not found", "status": "FAILED"})

        serializer = StudentSerializer(instance=student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK,
                            data={"message": "student's record updated",
                                  "data": serializer.data,
                                  "status": "SUCCESS"})
        return Response(data={"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk=None):
        student = self.get_object(pk)
        if student is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "student's record not found", "status": "FAILED"})

        student.delete()
        user = User.objects.get(user_id=student.user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={"message": "student's record deleted", "status": "SUCCESS"})
