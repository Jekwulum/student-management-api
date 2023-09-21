from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from curriculumManagement.models import Class, Subject
from .serializers import ClassSerializer, SubjectSerializer


class ClassListView(APIView):
    def get(self, request: Request):
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Classes records retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    def post(self, request: Request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Class record created successfully", "status": "SUCCESS"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": serializer.errors, "status": "FAILED"})


class ClassDetailVIew(APIView):
    pass


class SubjectListView(APIView):
    def get(self, request: Request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Subjects records retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    def post(self, request: Request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Subject record created successfully", "status": "SUCCESS"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": serializer.errors, "status": "FAILED"})


class SubjectDetailView(APIView):
    pass
