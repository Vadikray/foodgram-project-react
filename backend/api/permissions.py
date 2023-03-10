from rest_framework import permissions


class AuthorRecipeEditPermissions(permissions.BasePermission):
    '''Пермишены для Рецептов.'''

    message = 'Для редактирования Вы должны быть автором контента.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if (request.method not in permissions.SAFE_METHODS
                and request.user.is_authenticated):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_staff
            or request.user.is_superuser
            or obj.author == request.user)
