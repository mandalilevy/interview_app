# Demo Application - Classroom Feedback System
## How to Run This Project
### 1. Clone repository
git clone <repo-url>
cd interview_app
### 2. Create virtual environment
python -m venv myenv
Activate:
- Windows:
myenv\Scripts\activate
### 3. Install dependencies
pip install -r requirements.txt
### 4. Create `.env` file
Create a file named `.env` in the **root of interview_app**:
interview_app/.env, Add:
DB_NAME=demo_db
DB_USER=postgres
DB_PASSWORD=123
DB_HOST=localhost
DB_PORT=5432
### 5. Run migrations
python manage.py makemigrations
python manage.py migrate
### 6. Seed the database
python manage.py seed
This creates:
- Instructor
- Student
- Observer
- Assignments
- Submissions
- Observer → Student link
### 7. Run development server
python manage.py runserver
## API Testing (Postman)
Base URL: http://127.0.0.1:8000/api/v1/
## Authentication
### Login
POST /auth/login/
### Refresh Token
POST /auth/refresh/
## Core Endpoints
### Assignments
GET /assignments/
POST /assignments/ (Instructor only)
### Submissions
POST /submissions/ (Student only)
GET /submissions/{id}/feedback/
PATCH /submissions/{id}/feedback/ (Instructor only)
## How to Break This App
This section highlights known limitations and security considerations.
### 1. Weak role enforcement in some endpoints
If permission classes are not properly attached to views, users could potentially access restricted endpoints.
**Fix:**
Always enforce DRF `permission_classes` at both view and object levels.
### 2. Observer scalability limitation
The current observer system supports only one student per observer.
This limits flexibility in real-world scenarios where:
- a parent may have multiple students
**Fix:**
Replace `OneToOneField` with a `ManyToManyField` and redesign permission logic.
## Teaching Comment Location
A teaching comment has been added inside: users/models.py, users/permissions.py, interview_app/settings.py
## Notes
This application is intentionally designed to demonstrate:
- Secure API design
- Progressive authorization models
- Real-world DRF permission architecture
