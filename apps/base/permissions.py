from rest_framework.permissions import BasePermission


class IsStudentUser(BasePermission):

    def has_permission(self, request, view):
        # permission for only GET requests if the user's type is 3.
        return bool(
            request.method == 'GET' and
            int(request.user.user_type)==3 and 
            request.user.is_active
        )