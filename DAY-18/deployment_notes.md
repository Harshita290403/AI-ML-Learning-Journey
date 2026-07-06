# Deployment Notes

## Development vs Production

| Development | Production |
|-------------|------------|
| Used for building and testing the application. | Used by real users in a live environment. |
| `DEBUG=True` | `DEBUG=False` |
| Detailed error messages are displayed. | Generic error pages are shown to users. |
| Usually runs on a local machine. | Hosted on cloud platforms such as Render, Railway, AWS, or Azure. |
| Focuses on development and debugging. | Focuses on security, performance, and reliability. |

---

## Environment Variables Used

The project stores sensitive configuration values in a `.env` file instead of hardcoding them in the source code.

Current environment variables:

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

### Description

- **SECRET_KEY**: Used by Django for cryptographic signing, sessions, password reset tokens, and other security-related features. It must remain confidential.
- **DEBUG**: Controls whether Django runs in development mode (`True`) or production mode (`False`).

A `.env.example` file is included to provide a template for configuring these variables without exposing sensitive information.

---

## Steps to Prepare a Django Project for Deployment

1. Move sensitive information such as `SECRET_KEY` and `DEBUG` to environment variables.
2. Create a `.env.example` file for other developers.
3. Add `.env` to `.gitignore` to prevent accidental commits.
4. Set `DEBUG=False` before deploying.
5. Configure `ALLOWED_HOSTS` with the application's domain or server IP.
6. Install project dependencies using `requirements.txt`.
7. Apply database migrations:

```bash
python manage.py migrate
```

8. Collect static files (if the project includes them):

```bash
python manage.py collectstatic
```

9. Test all API endpoints to ensure they work correctly.
10. Verify Swagger/OpenAPI documentation is accessible.
11. Review authentication, permissions, validation, and error handling.
12. Deploy the application to a hosting platform such as Render, Railway, AWS, or Azure.

---

## Summary

This project follows several deployment best practices, including:

- Environment variable configuration using `python-decouple`
- Interactive API documentation with `drf-spectacular`
- JWT Authentication
- Input validation
- Pagination
- Professional error handling
- Secure configuration through `.env` files