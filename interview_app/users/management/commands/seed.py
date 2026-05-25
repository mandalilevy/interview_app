from django.core.management.base import BaseCommand

from users.models import User, ObserverStudentLink
from assignments.models import Assignment
from submissions.models import Submission

# this class will pre-populating your database with an initial set of data.
# This saves you time when testing your APIs
class Command(BaseCommand):

    help = "Seeds the database with demo data"

    def handle(self, *args, **kwargs):

        self.stdout.write("Seeding database...")


        instructor, created = User.objects.get_or_create(
            username="instructor",
            defaults={
                "email": "instructor@demo.dev",
                "role": "INSTRUCTOR"
            }
        )

        instructor.set_password("Demo@1234")
        instructor.save()

        student, created = User.objects.get_or_create(
            username="student",
            defaults={
                "email": "student@demo.dev",
                "role": "STUDENT"
            }
        )

        student.set_password("Demo@1234")
        student.save()

        observer, created = User.objects.get_or_create(
            username="observer",
            defaults={
                "email": "observer@demo.dev",
                "role": "OBSERVER"
            }
        )

        observer.set_password("Demo@1234")
        observer.save()

     
        student2, created = User.objects.get_or_create(
            username="student2",
            defaults={
                "email": "student2@demo.dev",
                "role": "STUDENT"
            }
        )

        student2.set_password("Demo@1234")
        student2.save()

        ObserverStudentLink.objects.get_or_create(
            observer=observer,
            student=student
        )

   
        assignment1, created = Assignment.objects.get_or_create(
            title="JWT Authentication",
            defaults={
                "description": "Learn JWT basics",
                "instructor": instructor
            }
        )

        assignment2, created = Assignment.objects.get_or_create(
            title="DRF Permissions",
            defaults={
                "description": "Learn DRF permissions",
                "instructor": instructor
            }
        )

    
        Submission.objects.get_or_create(
            assignment=assignment1,
            student=student,
            defaults={
                "content": "My JWT assignment",
                "feedback": "Excellent work"
            }
        )

        Submission.objects.get_or_create(
            assignment=assignment2,
            student=student,
            defaults={
                "content": "My permissions assignment",
                "feedback": "Very good understanding"
            }
        )

        Submission.objects.get_or_create(
            assignment=assignment1,
            student=student2,
            defaults={
                "content": "Another student's work",
                "feedback": "Needs improvement"
            }
        )

        self.stdout.write(
            self.style.SUCCESS("Database seeded successfully!")
        )