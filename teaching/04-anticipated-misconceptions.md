# ANTICIPATED MISCONCEPTIONS

##### Misconception 1: “Authentication and authorization are the same thing”

Why learners think this: Because both happen during login and API access.

Correction:

* Authentication = identity
* Authorization = permissions

##### Misconception 2: “JWT makes the system automatically secure”

Why learners think this: Because token feels like a security feature.

Correction:

* JWT only proves identity
* You must still enforce permissions in backend

##### Misconception 3: “If a user is logged in, they can access everything”

Why learners think this: Because login feels like full access.

Correction:

* Student login works
* But assignment creation fails (403)

