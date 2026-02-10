from rest_framework import permissions

class IsEmployerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests (Read-only) for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to authenticated users
        if not request.user.is_authenticated:
            return False

        # Check if the user has the 'EMPLOYER' role
        return request.user.role == 'EMPLOYER'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the job
        # This prevents Employer A from editing Employer B's job
        return obj.employer == request.user
