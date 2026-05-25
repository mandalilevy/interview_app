# Classroom Feedback System (Django + DRF + JWT RBAC Demo)
## Overview
This project is a Django REST Framework-based classroom feedback system built to demonstrate:
- JWT-based authentication
- Role-Based Access Control (RBAC)
- Row-level permissions
- Secure API design using Django REST Framework
The system simulates a real classroom environment with three roles:
- **Instructor** → creates assignments and gives feedback
- **Student** → submits assignments and views feedback
- **Observer** → views a single student's progress (row-level restricted access)
## Tech Stack
- Django
- Django REST Framework
- SimpleJWT (JWT Authentication)
- PostgreSQL
- Python
## Demo Credentials
### Instructor
Email: instructor@demo.dev
Password: Demo@1234
### Student
Email: student@demo.dev
Password: Demo@1234
### Observer
Email: observer@demo.dev
Password: Demo@1234
## How to Navigate This Submission
### 1. Demo Application (backend)
Located in: /interview_app

Contains:
- Django project
- API endpoints
- Authentication system
- Permission logic
### 2. Teaching Package
Located in: /teaching-package
Includes:
- `01-session-outline.md` → 60-minute teaching plan
- `02-learning-objectives.md` → measurable learning outcomes
- `03-concept-explainers.md` → JWT, RBAC, row-level security explanation
- `04-anticipated-misconceptions.md` → common learner misunderstandings
## Key Features Demonstrated
- JWT Authentication (login + refresh)
- Custom User model with roles
- Role-based access control (Instructor, Student, Observer)
- Row-level permissions for secure data access
- Observer restricted to a single student only
- Secure feedback system
## API Base URL: /api/v1/
## Authentication Flow
1. User logs in via: POST /api/v1/auth/login/
2. Receives:
- Access token
- Refresh token
3. Uses token in requests: Authorization: Bearer <access_token>
## Security Concepts Demonstrated
- Authentication vs Authorization
- Role-based access control
- Object-level (row-level) permissions
- Secure token-based API authentication
## Author Notes
This project was designed as a teaching demonstration to show how secure APIs evolve from simple role checks to full object-level security systems.
