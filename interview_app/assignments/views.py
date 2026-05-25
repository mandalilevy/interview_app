from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Assignment
from .serializers import AssignmentSerializer

from users.permissions import IsInstructor
from users.models import ObserverStudentLink


class AssignmentListCreateView(generics.ListCreateAPIView):

    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.role == "INSTRUCTOR":
            return Assignment.objects.filter(instructor=user)

        if user.role == "STUDENT":
            return Assignment.objects.all()

        if user.role == "OBSERVER":

            link = ObserverStudentLink.objects.filter(
                observer=user
            ).first()

            if link:
                return Assignment.objects.filter(
                    submissions__student=link.student
                ).distinct()

        return Assignment.objects.none()

    def perform_create(self, serializer):

        if self.request.user.role != "INSTRUCTOR":
            raise PermissionDenied(
                "Only instructors can create assignments."
            )

        serializer.save(instructor=self.request.user)