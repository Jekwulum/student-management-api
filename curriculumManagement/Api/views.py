from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from curriculumManagement.models import Class, Subject, Result
from .serializers import ClassSerializer, SubjectSerializer, ResultSerializer
from django.db.models import Q


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
    def get_object(self, pk=None):
        try:
            student_class = Class.objects.get(class_id=pk)
            return student_class
        except Class.DoesNotExist:
            return None

    def get(self, request: Request, pk=None):
        student_class = self.get_object(pk)
        if student_class is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Class record not found", "status": "FAILED"})

        serializer = ClassSerializer(student_class)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Class' record retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    def patch(self, request: Request, pk=None):
        student_class = self.get_object(pk)
        if student_class is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Class record not found", "status": "FAILED"})
        serializer = ClassSerializer(
            instance=student_class, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK,
                            data={"message": "Class' record updated",
                                  "data": serializer.data,
                                  "status": "SUCCESS"})
        return Response(data={"message": serializer.errors, "status": "FAILED"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk=None):
        student_class = self.get_object(pk)
        if student_class is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Class record not found", "status": "FAILED"})

        student_class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={"message": "Subject's record deleted", "status": "SUCCESS"})


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
    def get_object(self, pk=None):
        try:
            subject = Subject.objects.get(Q(code=pk) | Q(subject_id=pk))
            return subject
        except Subject.DoesNotExist:
            return None

    def get(self, request: Request, pk=None):
        subject = self.get_object(pk)
        if subject is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Subject's record not found", "status": "FAILED"})

        serializer = SubjectSerializer(subject)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Subject's record retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    def patch(self, request: Request, pk=None):
        subject = self.get_object(pk)
        if subject is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Subject's record not found", "status": "FAILED"})
        serializer = SubjectSerializer(
            instance=subject, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK,
                            data={"message": "Subject's record updated",
                                  "data": serializer.data,
                                  "status": "SUCCESS"})
        return Response(data={"message": serializer.errors, "status": "FAILED"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk=None):
        subject = self.get_object(pk)
        if subject is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Subject record not found", "status": "FAILED"})

        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={"message": "Subject's record deleted", "status": "SUCCESS"})


class ResultListView(APIView):
    def get(self, request: Request):
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Results records retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    def post(self, request: Request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Result record created successfully", "status": "SUCCESS"})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": serializer.errors, "status": "FAILED"})


class ResultDetailView(APIView):
    def get_object(self, pk=None):
        try:
            result = Result.objects.get(result_id=pk)
            return result
        except Result.DoesNotExist:
            return None

    def get(self, request: Request, pk=None):
        result = self.get_object(pk)
        if result is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Result record not found", "status": "FAILED"})

        serializer = ResultSerializer(result)
        return Response(status=status.HTTP_200_OK,
                        data={"message": "Result record retrieved successfully",
                              "status": "SUCCESS",
                              "data": serializer.data})

    def patch(self, request: Request, pk=None):
        result = self.get_object(pk)
        if result is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Result record not found", "status": "FAILED"})
        serializer = ResultSerializer(
            instance=result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK,
                            data={"message": "Result record updated",
                                  "data": serializer.data,
                                  "status": "SUCCESS"})
        return Response(data={"message": serializer.errors, "status": "FAILED"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk=None):
        result = self.get_object(pk)
        if result is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"message": "Result record not found", "status": "FAILED"})

        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={"message": "Result record deleted", "status": "SUCCESS"})
