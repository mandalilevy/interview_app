# LEARNING OBJECTIVES

#### ***Objective* 1: Implement JWT authentication in a Django REST API**

##### Learners will:

* Configure SimpleJWT
* Obtain access and refresh tokens via login endpoint

##### Assessment:

Learner can successfully:

* Send login request in Postman
* Receive valid JWT tokens
* Use token to access protected endpoint

#### **Objective 2: Differentiate authentication and authorization in practice**

##### Learners will:

* Explain the difference between identity verification and access control
* Identify where each occurs in the system

##### Assessment:

Learner can:

* Correctly classify login vs permission logic in code
* Explain why a user gets a 403 error

#### **Objective 3: Implement role-based access control using DRF permission classes**

##### Learners will:

* Create custom permissions for Instructor, Student, Observer
* Restrict endpoint access based on roles

##### Assessment:

Learner can:

* Block student from creating assignments
* Allow instructor-only operations

#### **Objective 4: Apply row-level permissions for data security**

##### Learners will:

* Restrict access to specific database rows based on relationships

##### Assessment:

Learner can:

* Ensure observer only accesses linked student data
* Prevent cross-user data leakage

#### **Objective 5: Use JWT tokens to access protected API endpoints via Postman**

##### Learners will:

* Attach Bearer tokens in requests
* Refresh expired tokens

##### Assessment:

Learner can:

* Successfully refresh token
* Maintain authenticated session across requests

