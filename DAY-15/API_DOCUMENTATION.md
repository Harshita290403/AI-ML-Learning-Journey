# Student Management REST API Documentation

| Endpoint            | Method | Auth Required | Description          |
|---------------------|--------|---------------|----------------------|
| /api/token/         | POST   | No            | Generate JWT Token   |
| /api/token/refresh/ | POST   | No            | Refresh Access Token |
| /api/students/      | GET    | Yes           | View all students    |
| /api/students/      | POST   | Yes           | Add new student      |
| /api/students/<id>/ | GET    | Yes           | Retrieve student     |
| /api/students/<id>/ | PUT    | Yes           | Update student       |
| /api/students/<id>/ | DELETE | Yes           | Delete student       |


## Create Student

### Request

POST /api/students/

```json
{
    "name":"Harshita",
    "age":21,
    "course":"AI & Data Science"
}
```

### Response

```json
{
    "id":1,
    "name":"Harshita",
    "age":21,
    "course":"AI & Data Science"
}
```

---

## Search Student

GET

```
/api/students/?search=Harshita
```

---

## Filter Student

GET

```
/api/students/?course=AI & Data Science
```

---

## Order by Age

GET

```
/api/students/?ordering=age
```

---

## Why API Documentation is Important

- Helps frontend developers understand endpoints quickly.
- Reduces communication gaps.
- Makes testing easier.
- Speeds up onboarding of new developers.
- Acts as a reference for future maintenance.