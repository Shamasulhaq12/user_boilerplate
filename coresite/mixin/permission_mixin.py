from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """
    Custom permission to only allow admin users to access.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.user_type == 'admin'
