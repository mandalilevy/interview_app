from rest_framework.permissions import BasePermission
from users.models import ObserverStudentLink

# We now define custom permission classes in DRF to control which users 
# are allowed to access certain parts of the application based on their role:
# (Instructor, Student, or Observer).
class IsInstructor(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "INSTRUCTOR"


class IsStudent(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "STUDENT"


class SubmissionFeedbackPermission(BasePermission):


    def has_object_permission(self, request, view, obj):

        user = request.user

        if user.role == "STUDENT":
            return obj.student == user

        if user.role == "INSTRUCTOR":
            return obj.assignment.instructor == user

        if user.role == "OBSERVER":

            return ObserverStudentLink.objects.filter(
                observer=user,
                student=obj.student
            ).exists()

        return False