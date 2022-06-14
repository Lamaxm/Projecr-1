from rest_framework.permissions import BasePermission

class IsOwn(BasePermission):
    """Parmission to verify that the current user is the owner of the account"""
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

