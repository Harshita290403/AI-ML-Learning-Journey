# API Endpoints

## Protected Endpoints

| Method | Endpoint                  |
| ------ | ------------------------- |
| GET    | `/api/students/`          |
| POST   | `/api/students/`          |
| GET    | `/api/students/<id>/`     |
| PUT    | `/api/students/<id>/`     |
| PATCH  | `/api/students/<id>/`     |
| DELETE | `/api/students/<id>/`     |
| GET    | `/api/profile/` *(Bonus)* |

---

## Required Authorization Header

All protected APIs require the following header:

```http
Authorization: Token 9e57adf28ab5cb6936b0c7d9e4f9c0f3d0
```

Replace the token value with your generated token.

---

## Sample Unauthorized Request

### Request

```http
GET /api/students/
```

### Response

**Status Code:** `401 Unauthorized`

```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

## Sample Authorized Request

### Request

```http
GET /api/students/

Authorization: Token 9e57adf28ab5cb6936b0c7d9e4f9c0f3d0
```

### Response

**Status Code:** `200 OK`

```json
[
    {
        "id": 1,
        "name": "Harshita",
        "email": "harshita@gmail.com",
        "age": 21,
        "course": "AI & Data Science"
    }
]
```

---

## Sample Authorized POST Request

### Request

```http
POST /api/students/

Authorization: Token 9e57adf28ab5cb6936b0c7d9e4f9c0f3d0
```

Request Body

```json
{
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "age": 22,
    "course": "Machine Learning"
}
```

### Response

**Status Code:** `201 Created`

```json
{
    "id": 2,
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "age": 22,
    "course": "Machine Learning"
}
```
