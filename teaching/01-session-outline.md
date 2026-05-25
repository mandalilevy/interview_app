# SESSION OUTLINE: 60 MINUTES

##### **0–5 min: Context and Hook**

Show the working classroom feedback API system:

* Instructor creates assignments
* Student submits work
* Instructor leaves feedback
* Observer sees limited student progress

###### Purpose:

Learners first see the final system they are working toward. This creates motivation and gives context before introducing technical concepts.

##### **5–15 min: Introduction and Definition of Terms**

Introduce the core security concepts:

* Authentication (identity verification)
* Authorization (permission control)
* Real-world examples of authentication and authorization

###### Example:

* Logging into a bank account = authentication
* Being allowed to transfer money = authorization

###### Purpose:

Build a strong mental model before learners begin implementing security features in code.

##### **15–30 min: JWT Authentication in Django REST Framework**

###### Topics covered:

* What a JWT token is
* Access tokens vs refresh tokens
* Why APIs commonly use JWT instead of session authentication
* How login endpoints work

###### Live Demo:

* Login request in Postman
* Receiving access and refresh tokens
* Using Bearer tokens in authenticated requests

###### Purpose:

Make token-based authentication practical and visible through live API interaction.

##### **30–45 min: Role-Based Access Control (RBAC)**

###### Topics covered:

Custom user roles:

* Instructor
* Student
* Observer
* DRF custom permission classes
* Protecting endpoints using roles

###### Live Demo:

* Student attempts instructor action → receives 403 Forbidden
* Instructor successfully creates assignment

###### Purpose:

Demonstrate how backend systems enforce permissions after a user has been authenticated.

##### **45–55 min: Row-Level Permissions (Observer Case Study)**

###### Topics covered:

* Difference between role-level and row-level permissions
* Observer linked to one specific student
* Restricting access to specific database records

###### Live Demo:

* Observer accesses linked student data → allowed
* Observer attempts other student data → forbidden

###### Purpose:

Introduce learners to real-world data protection patterns used in production systems.

##### **55–60 min: Recap and Questions**

###### Summary of key ideas:

* Authentication verifies identity
* Authorization controls actions
* Row-level permissions control access to specific data
* Open Q\&A and clarification.

###### Purpose:

Reinforce understanding and consolidate key concepts before learners continue independently.

##### **Why This Order Works**

This session follows a progressive learning structure:

* Learners first see the completed system to understand the practical goal.
* Core security concepts are introduced before implementation.
* JWT authentication is taught before permissions because authorization depends on knowing who the user is.
* Role-based permissions are introduced before row-level permissions because row-level security is a more advanced extension of authorization.
* The session ends with recap and reflection to reinforce retention.

