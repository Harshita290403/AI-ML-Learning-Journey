# Student Management REST API Project Structure

## Folder Structure

backend_journey/
│
├── backend_journey/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── core/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── admin.py

---

## Purpose of Each File

### models.py
Defines the Student database model.

### serializers.py
Converts model objects into JSON and validates incoming data.

### views.py
Contains API logic such as Create, Read, Update and Delete operations.

### urls.py
Maps URLs to corresponding API views.

### settings.py
Configures installed apps, JWT authentication, database, and REST Framework settings.

### admin.py
Registers models for Django Admin Panel.

---

## Request Flow

Client Request

↓

URL

↓

View

↓

Serializer

↓

Model

↓

Database

↓

Serializer

↓

JSON Response

## Project Approach

1. Created the Student model.
2. Built serializers for data validation.
3. Implemented CRUD APIs.
4. Added Search, Filter and Ordering.
5. Protected APIs using JWT Authentication.
6. Tested every endpoint using Postman.
7. Prepared API documentation.

## Importance of Clean Project Organization

- Improves code readability.
- Makes debugging easier.
- Encourages code reusability.
- Simplifies collaboration among developers.
- Makes future maintenance easier.