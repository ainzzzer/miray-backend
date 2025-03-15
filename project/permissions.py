from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "client")


class IsClientWithPerm(BasePermission):
    def has_permission(self, request, view):
        return (
            hasattr(request.user, "client")
            and bool(request.user.client.has_permission)
        )


class IsClientWithPermReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            and hasattr(request.user, "client")
            and bool(request.user.client.has_permission)
        )


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, "staff")


class IsStaffOrClientWithPermReadOnly(BasePermission):
    """
    GET запросы для клиентов с доступом.

    Запросы на изменение данных только для сотрудников.
    """

    def has_permission(self, request, view):
        return (
            (
                request.method in SAFE_METHODS
                and hasattr(request.user, "client")
                and bool(request.user.client.has_permission)
            )
            or hasattr(request.user, "staff")
        )
