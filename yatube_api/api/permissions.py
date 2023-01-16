from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Пользовательские разрешения.

    Не авторизированные пользователи, только просматривают контент авторов
    и оставляют комментарии.
    Авторы постов и комментариев могут редактировать только свои записи.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
