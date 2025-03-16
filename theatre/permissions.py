from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
            or request.user.is_staff
        )
