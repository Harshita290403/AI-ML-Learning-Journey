# Student API Endpoints

Base URL:

```
http://127.0.0.1:8000/api/students/
```

---

## 1. Get All Students

**Endpoint**

```
GET /api/students/
```

### Sample Request

```http
GET http://127.0.0.1:8000/api/students/
```

### Sample Response

```json
[
    {
        "id": 1,
        "name": "Harshita",
        "email": "harshita@gmail.com",
        "age": 21,
        "course": "CSE"
    },
    {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com",
        "age": 22,
        "course": "AI"
    }
]
```

---

## 2. Search Students

Search students by **Name** or **Course**.

**Endpoint**

```
GET /api/students/?search=<keyword>
```

### Sample Request

```http
GET http://127.0.0.1:8000/api/students/?search=Harshita
```

or

```http
GET http://127.0.0.1:8000/api/students/?search=AI
```

### Sample Response

```json
[
    {
        "id": 1,
        "name": "Harshita",
        "email": "harshita@gmail.com",
        "age": 21,
        "course": "CSE"
    }
]
```

---

## 3. Filter Students by Course

**Endpoint**

```
GET /api/students/?course=<course_name>
```

### Sample Request

```http
GET http://127.0.0.1:8000/api/students/?course=AI
```

### Sample Response

```json
[
    {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com",
        "age": 22,
        "course": "AI"
    }
]
```

---

## 4. Order Students by Age (Ascending)

**Endpoint**

```
GET /api/students/?ordering=age
```

### Sample Request

```http
GET http://127.0.0.1:8000/api/students/?ordering=age
```

### Sample Response

```json
[
    {
        "id": 3,
        "name": "Aman",
        "age": 19,
        "course": "CSE"
    },
    {
        "id": 1,
        "name": "Harshita",
        "age": 21,
        "course": "CSE"
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 22,
        "course": "AI"
    }
]
```

---

## 5. Order Students by Name (Descending)

**Endpoint**

```
GET /api/students/?ordering=-name
```

### Sample Request

```http
GET http://127.0.0.1:8000/api/students/?ordering=-name
```

### Sample Response

```json
[
    {
        "id": 2,
        "name": "Rahul",
        "age": 22,
        "course": "AI"
    },
    {
        "id": 1,
        "name": "Harshita",
        "age": 21,
        "course": "CSE"
    },
    {
        "id": 3,
        "name": "Aman",
        "age": 19,
        "course": "CSE"
    }
]
```

---

## 6. Create a Student

**Endpoint**

```
POST /api/students/
```

### Sample Request

```http
POST http://127.0.0.1:8000/api/students/
Content-Type: application/json
```

### Request Body

```json
{
    "name": "Priya",
    "email": "priya@gmail.com",
    "age": 20,
    "course": "AI"
}
```

### Sample Response

```json
{
    "id": 4,
    "name": "Priya",
    "email": "priya@gmail.com",
    "age": 20,
    "course": "AI"
}
```

---

## 7. Update a Student

**Endpoint**

```
PUT /api/students/<id>/
```

### Sample Request

```http
PUT http://127.0.0.1:8000/api/students/4/
Content-Type: application/json
```

### Request Body

```json
{
    "name": "Priya Sharma",
    "email": "priya@gmail.com",
    "age": 21,
    "course": "CSE"
}
```

### Sample Response

```json
{
    "id": 4,
    "name": "Priya Sharma",
    "email": "priya@gmail.com",
    "age": 21,
    "course": "CSE"
}
```

---

## 8. Delete a Student

**Endpoint**

```
DELETE /api/students/<id>/
```

### Sample Request

```http
DELETE http://127.0.0.1:8000/api/students/4/
```

### Sample Response

```http
HTTP 204 No Content
```

Response Body

```json
{}
```

---

# Query Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `search` | Search students by name or course | `?search=Harshita` |
| `course` | Filter students by course | `?course=AI` |
| `ordering=age` | Sort students by age (ascending) | `?ordering=age` |
| `ordering=-name` | Sort students by name (descending) | `?ordering=-name` |

---

# HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| **200 OK** | Request successful |
| **201 Created** | Student created successfully |
| **204 No Content** | Student deleted successfully |
| **400 Bad Request** | Invalid input data |
| **404 Not Found** | Student not found |