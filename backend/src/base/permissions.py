from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.is_admin

class IsAdminOrReadOnly(IsAuthenticated):
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_admin
        )
