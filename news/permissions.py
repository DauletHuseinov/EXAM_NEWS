from rest_framework.permissions import BasePermission, SAFE_METHODS


# class IsNewsPermissions(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return bool(
#             request.method in SAFE_METHODS or
#             (request.user and request.user.is_authenticated and request.user.profile.is_author)
#         )


class IsAuthorPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and request.user.is_authenticated and request.user.author)
        )
