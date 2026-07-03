# API Endpoints Documentation

## 1. User Registration

**Endpoint**

```
POST /api/register/
```

**Authentication Required**

No

### Sample Request

```json
{
    "username": "harshita",
    "email": "harshita@gmail.com",
    "password": "password123"
}
```

### Sample Response

```json
{
    "message": "User registered successfully.",
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

---

## 2. User Login

**Endpoint**

```
POST /api/login/
```

**Authentication Required**

No

### Sample Request

```json
{
    "username": "harshita",
    "password": "password123"
}
```

### Sample Response

```json
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```

---

## 3. Current User Profile

**Endpoint**

```
GET /api/profile/
```

**Authentication Required**

Yes (JWT Access Token)

### Request Header

```
Authorization: Bearer <access_token>
```

### Sample Response

```json
{
    "username": "harshita",
    "email": "harshita@gmail.com",
    "date_joined": "2026-07-03T10:30:15.123456Z"
}
```