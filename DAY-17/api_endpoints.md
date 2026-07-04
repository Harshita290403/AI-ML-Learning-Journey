# Student Management API Documentation

## Base URL

```
http://127.0.0.1:8000/api/
```

---

# Authentication

Most endpoints require JWT Authentication.

**Header**

```
Authorization: Bearer <access_token>
```

---

# API Endpoints

## 1. Register User

**POST** `/api/register/`

### Sample Request

```json
{
    "username": "harshita",
    "email": "harshita@gmail.com",
    "password": "password123"
}
```

### Success Response (201 Created)

```json
{
    "message": "User registered successfully.",
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

---

## 2. Login User

**POST** `/api/login/`

### Sample Request

```json
{
    "username": "harshita",
    "password": "password123"
}
```

### Success Response (200 OK)

```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

---

## 3. Get User Profile

**GET** `/api/profile/`

**Authentication Required**

### Success Response

```json
{
    "username": "harshita",
    "email": "harshita@gmail.com",
    "date_joined": "2026-07-04T10:00:00Z"
}
```

---

## 4. Get All Students

**GET** `/api/students/`

### Pagination Examples

Default page:

```
GET /api/students/?page=1
```

Custom page size:

```
GET /api/students/?page=1&page_size=10
```

Next page:

```
GET /api/students/?page=2&page_size=10
```

---

## 5. Create Student

**POST** `/api/students/`

**Authentication Required**

### Sample Request

```json
{
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "age": 20,
    "course": "Python"
}
```

### Success Response (201 Created)

```json
{
    "id": 1,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "age": 20,
    "course": "Python"
}
```

---

## 6. Get Single Student

**GET** `/api/students/<id>/`

---

## 7. Update Student

**PUT** `/api/students/<id>/`

**Authentication Required**

---

## 8. Delete Student

**DELETE** `/api/students/<id>/`

**Authentication Required**

---

# Validation Rules

| Field | Validation |
|--------|------------|
| Name | Cannot contain numbers |
| Age | Must be at least 18 years |
| Email | Must be unique |
| Course | Cannot be empty |
| Password | Minimum 8 characters |

---

# Pagination

Default page size:

```
5 students
```

Custom page size:

```
GET /api/students/?page=1&page_size=10
```

Maximum page size:

```
20 students
```

---

# Sample Error Responses

## Student Not Found

**Status:** 404 Not Found

```json
{
    "error": "Student with the given ID does not exist."
}
```

---

## Invalid Age

**Status:** 400 Bad Request

```json
{
    "error": {
        "age": [
            "Student must be at least 18 years old."
        ]
    }
}
```

---

## Duplicate Email

**Status:** 400 Bad Request

```json
{
    "error": {
        "email": [
            "Email already exists."
        ]
    }
}
```

---

## Invalid Name

**Status:** 400 Bad Request

```json
{
    "error": {
        "name": [
            "Name cannot contain numbers."
        ]
    }
}
```

---

## Empty Course

**Status:** 400 Bad Request

```json
{
    "error": {
        "course": [
            "Course cannot be empty."
        ]
    }
}
```

---

## Unauthorized Access

**Status:** 401 Unauthorized

```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

# HTTP Status Codes Used

| Status Code | Meaning |
|-------------|---------|
| 200 OK | Request successful |
| 201 Created | Resource created successfully |
| 400 Bad Request | Invalid input data |
| 401 Unauthorized | Authentication required |
| 404 Not Found | Resource does not exist |
