# Student Management API

A RESTful API built with Django REST Framework for managing student records. The project includes authentication, CRUD operations, validation, pagination, filtering, and interactive API documentation using Swagger.

---

## Features

- Student CRUD Operations
- JWT Authentication (Login & Registration)
- User Profile API
- Serializer Validation
- Pagination
- Filtering
- Professional Error Handling
- Interactive Swagger Documentation
- OpenAPI Schema Generation
- Environment Variable Configuration

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Simple JWT
- drf-spectacular
- python-decouple

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd backend_journey
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file using `.env.example`.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run the Server

```bash
python manage.py runserver
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/api/docs/
```

OpenAPI Schema

```
http://127.0.0.1:8000/api/schema/
```

---

## Authentication

This project uses JWT Authentication.

### Register

POST

```
/api/register/
```

### Login

POST

```
/api/login/
```

After logging in, include the access token in the request header:

```
Authorization: Bearer <your_access_token>
```

---

## Sample API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/register/ | Register a new user |
| POST | /api/login/ | Login user |
| GET | /api/profile/ | Get user profile |
| GET | /api/students/ | List all students |
| POST | /api/students/ | Create student |
| GET | /api/students/{id}/ | Retrieve student |
| PUT | /api/students/{id}/ | Update student |
| PATCH | /api/students/{id}/ | Partially update student |
| DELETE | /api/students/{id}/ | Delete student |

---

## License

This project is created for learning and educational purposes.