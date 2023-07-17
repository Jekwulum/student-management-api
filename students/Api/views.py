import random
import datetime
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from students.models import Student
from .serializers import StudentSerializer


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
    def get(self, request: Request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Students records retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    def post(self, request: Request):
        data = request.data
        number = random.randint(0, 9999)
        data['registrationNo'] = f"{datetime.date.today().year}-STU-{number:04}"
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Student created successfully", "status": "SUCCESS"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": serializer.errors, "status": "FAILED"})


class StudentDetailView(APIView):
    def get_object(self, pk=None):
        try:
            student = Student.objects.get(Q(studentId=pk))
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
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={"message": "student's record deleted", "status": "SUCCESS"})
