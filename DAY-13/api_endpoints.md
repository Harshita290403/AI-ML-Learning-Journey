# API Endpoints Documentation

## Base URL

```text
http://127.0.0.1:8000/
```

---

# Authentication Endpoints

## 1. Obtain JWT Token

**Endpoint**

```http
POST /api/token/
```

### Request Body

```json
{
    "username": "harshita",
    "password": "your_password"
}
```

### Successful Response (200 OK)

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIs...",
    "access": "eyJhbGciOiJIUzI1NiIs..."
}
```

### Failed Response (401 Unauthorized)

```json
{
    "detail": "No active account found with the given credentials"
}
```

---

## 2. Refresh Access Token

**Endpoint**

```http
POST /api/token/refresh/
```

### Request Body

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```

### Successful Response (200 OK)

```json
{
    "access": "eyJhbGciOiJIUzI1NiIs..."
}
```

### Failed Response (401 Unauthorized)

```json
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```

---

# Student API Endpoints

## 1. Get All Students

```http
GET /api/students/
```

**Authorization Header**

```text
Authorization: Bearer <access_token>
```

### Success Response

```json
[
    {
        "id": 1,
        "name": "Harshita",
        "email": "harshita@example.com",
        "age": 21,
        "course": "AI & Data Science"
    }
]
```

---

## 2. Create Student

```http
POST /api/students/
```

**Authorization Header**

```text
Authorization: Bearer <access_token>
```

### Request Body

```json
{
    "name": "Harshita",
    "email": "harshita@example.com",
    "age": 21,
    "course": "AI & Data Science"
}
```

### Success Response

```json
{
    "id": 1,
    "name": "Harshita",
    "email": "harshita@example.com",
    "age": 21,
    "course": "AI & Data Science"
}
```

---

## 3. Get Student by ID

```http
GET /api/students/<id>/
```

Example:

```http
GET /api/students/1/
```

**Authorization Header**

```text
Authorization: Bearer <access_token>
```

### Success Response

```json
{
    "id": 1,
    "name": "Harshita",
    "email": "harshita@example.com",
    "age": 21,
    "course": "AI & Data Science"
}
```

---

## 4. Update Student (PUT)

```http
PUT /api/students/<id>/
```

**Authorization Header**

```text
Authorization: Bearer <access_token>
```

### Request Body

```json
{
    "name": "Harshita",
    "email": "harshita@example.com",
    "age": 22,
    "course": "Machine Learning"
}
```

### Success Response

```json
{
    "id": 1,
    "name": "Harshita",
    "email": "harshita@example.com",
    "age": 22,
    "course": "Machine Learning"
}
```

---

## 5. Update Student (PATCH)

```http
PATCH /api/students/<id>/
```

**Authorization Header**

```text
Authorization: Bearer <access_token>
```

### Request Body

```json
{
    "course": "AI & Data Science"
}
```

### Success Response

```json
{
    "id": 1,
    "name": "Harshita",
    "email": "harshita@example.com",
    "age": 22,
    "course": "AI & Data Science"
}
```

---

## 6. Delete Student

```http
DELETE /api/students/<id>/
```

Example:

```http
DELETE /api/students/1/
```

**Authorization Header**

```text
Authorization: Bearer <access_token>
```

### Success Response

```json
{
    "message": "Student deleted successfully."
}
```

or

```http
204 No Content
```

---

# Authorization Header for Protected Endpoints

All student endpoints require a valid JWT Access Token.

```text
Authorization: Bearer <your_access_token>
```
