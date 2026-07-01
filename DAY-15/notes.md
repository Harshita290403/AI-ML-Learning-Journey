1. How to Structure a REST API Project
   -Separate code into apps based on functionality.
   -Keep models, serializers, views, URLs, and permissions in their respective files.
   -Follow a clear folder structure for maintainability and scalability.

2. Best Practices for Organizing Django Applications
   -Keep each app focused on a single responsibility.
   -Use reusable serializers, views, and utility functions.
   -Store configurations in settings.py and keep URLs modular.

3. Importance of API Documentation
   -Helps developers understand and use the API easily.
   -Documents endpoints, request/response formats, and authentication.
   -Simplifies testing, debugging, and future maintenance.

4. Writing Clean, Reusable Backend Code
   -Avoid code duplication by creating reusable components.
   -Use Django REST Framework generic views where appropriate.
   -Follow meaningful naming conventions and proper code formatting.

5. Common Mistakes to Avoid While Building APIs
   -Not validating input data.
   -Exposing unsecured endpoints.
   -Returning inconsistent response formats.
   -Ignoring proper error handling and HTTP status codes.

6. Key Learnings from the Project
   -Built a complete CRUD REST API using Django REST Framework.
   -Implemented JWT authentication, permissions, filtering, search, ordering, and pagination.
   -Learned how different DRF components work together in a real project.

7. Best Practices Followed
   -Used serializers for validation.
   -Secured endpoints with JWT authentication and permissions.
   -Organized code into models, serializers, views, and URLs.
   -Returned appropriate HTTP status codes and API responses.

8. Challenges Faced and How They Were Resolved
   -JWT authentication issues: Fixed by correctly configuring authentication classes and tokens.
   -Filtering and search not working: Resolved by adding DRF filter backends and configuring settings.
   -Permission errors: Fixed by assigning appropriate permission classes to each endpoint.

9. Areas for Future Improvement
   -Add Swagger/OpenAPI documentation.
   -Improve logging and exception handling.
   -Write unit and integration tests.
   -Implement caching and API rate limiting.
   -Add Docker deployment and CI/CD support.