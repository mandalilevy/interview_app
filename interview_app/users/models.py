from django.db import models
from django.contrib.auth.models import AbstractUser
# We now customize the Django user model to include a role-based system 
# (Instructor, Student, Observer) using an extended AbstractUser, 
# and it enforces email as the unique login field instead of a username.
class User(AbstractUser):

    class Roles(models.TextChoices):
        INSTRUCTOR = "INSTRUCTOR", "Instructor"
        STUDENT = "STUDENT", "Student"
        OBSERVER = "OBSERVER", "Observer"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices
    )

    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class ObserverStudentLink(models.Model):

    observer = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="observed_student"
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="observers"
    )

    def __str__(self):
        return f"{self.observer.email} -> {self.student.email}"
