from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate

from users.Api.serializers import CustomUserSerializer
from users.models import CustomUser
from users.permissions import IsStaffPermission


class UserListAV(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsStaffPermission]

    def get(self, request: Request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(
            data={"message": "users' records successfully fetched", "data": serializer.data, "status": "SUCCESS"},
            status=status.HTTP_200_OK)

    def post(self, request: Request):
        password = request.data["password"]
        confirm_password = request.data.pop("confirm_password")
        if password != confirm_password:
            return Response(data={'message': 'Passwords do not match!', 'status': 'FAILED'},
                            status=status.HTTP_400_BAD_REQUEST)

        if request.data.get("is_staff"):
            request.data["is_staff"] = True

        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "User added successfully", "data": serializer.data},
                            status=status.HTTP_200_OK)

        else:
            return Response(data={'message': serializer.errors, 'status': 'FAILED'},
                            status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, email):
        try:
            user = CustomUser.objects.get(email=email)
            return user
        except CustomUser.DoesNotExist:
            return None

    def get(self, request: Request, email):
        user = self.get_object(email)
        if user is None:
            return Response(data={"status": "FAILED", "message": "User does not exist"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = CustomUserSerializer(user)
        return Response(data={"status": "SUCCESS", "message": "User record retrieved", "data": serializer.data},
                        status=status.HTTP_200_OK)

    def patch(self, request: Request, email):
        instance = self.get_object(email)
        if instance is None:
            return Response(data={"status": "FAILED", "message": "User does not exist"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = CustomUserSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"status": "SUCCESS", "message": "User record updated", "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response(data={"status": "FAILED", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, email):
        user = self.get_object(email)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"status": "FAILED", "message": "student's record not found"})

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={"status": "SUCCESS", "message": "student's record deleted"})


class LoginAPIView(TokenObtainPairView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response({"status": "FAILED", "message": "Please provide both email and password."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)
        if not user:
            return Response({"status": "FAILED", "message": "Invalid login credentials"},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # user = serializer.user
            return Response({"status": "SUCCESS", "message": "Login successfully", "data": {
                "access": serializer.validated_data.get("access"),
                "refresh": serializer.validated_data.get("refresh"),
            }})

        return Response({"status": "FAILED", "message": serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LogoutAPIView(APIView):
    def post(self, request: Request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response({"status": "FAILED", "message": "Refresh token is required."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            TokenObtainPairView().token_blacklist[refresh_token]
            return Response({"status": "SUCCESS", "message": "Logged out successfully."})
        except KeyError:
            return Response({"status": "FAILED", "message": "Invalid refresh token."},
                            status=status.HTTP_400_BAD_REQUEST)
