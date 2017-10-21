from rest_framework import permissions


class IsHostOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow hosts to add/edit it.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.profile.is_host
