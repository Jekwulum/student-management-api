from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsStaffPermission(BasePermission):
    def has_permission(self, request: Request, view):
        print("request user: ", request.user, request.user.is_staff)
        return request.user.is_staff
