from django.urls import path
from .views import AssignmentListCreateView

urlpatterns = [
    path("", AssignmentListCreateView.as_view()),
]