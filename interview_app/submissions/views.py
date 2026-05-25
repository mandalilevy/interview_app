from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from .models import Submission
from .serializers import SubmissionSerializer
from rest_framework.exceptions import PermissionDenied
from users.permissions import (
    IsStudent,
    SubmissionFeedbackPermission
)


class SubmissionCreateView(generics.CreateAPIView):

    serializer_class = SubmissionSerializer

    permission_classes = [IsAuthenticated, IsStudent]

    def perform_create(self, serializer):

        serializer.save(student=self.request.user)


class SubmissionFeedbackView(generics.RetrieveAPIView):

    queryset = Submission.objects.all()

    serializer_class = SubmissionSerializer

    permission_classes = [
        IsAuthenticated,
        SubmissionFeedbackPermission
    ]


class SubmissionFeedbackUpdateView(UpdateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def perform_update(self, serializer):
        submission = self.get_object()

        if submission.assignment.instructor != self.request.user:
            raise PermissionDenied("Only instructor can give feedback")

        serializer.save()