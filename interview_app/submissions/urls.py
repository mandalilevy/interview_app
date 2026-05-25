from django.urls import path
from .views import (
    SubmissionCreateView,
    SubmissionFeedbackView, SubmissionFeedbackUpdateView
)

urlpatterns = [
    path("", SubmissionCreateView.as_view()),
    path(
        "<int:pk>/feedback/",
        SubmissionFeedbackView.as_view()
    ),
      path("<int:pk>/feedback/update/", SubmissionFeedbackUpdateView.as_view()),
]