from rest_framework import permissions

class IsApplicantOrEmployer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions (GET)
        if request.method in permissions.SAFE_METHODS:
            return (obj.applicant == request.user) or (obj.job.employer == request.user)

        # Write permissions (PUT/PATCH) - Only Employer can update status
        if request.method in ['PUT', 'PATCH']:
            return obj.job.employer == request.user

        return False
