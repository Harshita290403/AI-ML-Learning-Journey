1. Why API Validation is Important
   API validation ensures that only correct, complete, and safe data is accepted by the server. It prevents invalid data from being stored, improves security, and maintains data integrity.

2. Serializer Validation in DRF
   Serializer validation in Django REST Framework (DRF) checks incoming request data before it is saved. It validates fields, applies custom rules, and returns errors if the data is invalid.

3. Field-level vs Object-level Validation
   -> Field-level Validation: Validates a single field independently using methods like validate_<field_name>().
   -> Object-level Validation: Validates multiple fields together using the validate() method when fields depend on each other.

4. What is Pagination?
   Pagination is the process of dividing large datasets into smaller pages so that only a limited number of records are returned in each API response.

5. Why Production APIs Don't Return All Data at Once
   Returning all data at once can slow down the server, increase bandwidth usage, consume more memory, and create poor user experiences. Pagination improves performance and scalability.

6. Writing Meaningful Error Responses and Using Appropriate HTTP Status Codes
   Meaningful error responses clearly explain what went wrong so clients can fix the request. Appropriate HTTP status codes help applications understand the outcome of an API request.

   Common status codes:

   200 OK – Request successful.
   201 Created – Resource created successfully.
   400 Bad Request – Invalid request data.
   401 Unauthorized – Authentication required.
   403 Forbidden – Access denied.
   404 Not Found – Resource does not exist.
   500 Internal Server Error – Server-side error.

7. Why Shouldn't Backend Developers Rely Only on Frontend Validation?
   Frontend validation can be bypassed by users or malicious clients. Backend validation is essential because it guarantees that every request is validated before processing, regardless of its source.

8. What Problem Does Pagination Solve?
   Pagination reduces server load, speeds up API responses, lowers bandwidth usage, and makes large datasets easier for users to browse.

9. Which Validation Rule Was the Easiest to Implement?
   The easiest validation rule was field-level validation, as it checks a single field using a dedicated validation method like validate_age() or validate_name().

10. Why Are Proper Status Codes Important for Frontend Developers?
   Proper status codes help frontend applications identify whether a request succeeded or failed, allowing them to display appropriate messages, handle errors correctly, and improve the user experience.

11. Best Practices for API Error Handling
    .Return clear and descriptive error messages.
    .Use the correct HTTP status codes.
    .Validate all incoming data on the backend.
    .Avoid exposing sensitive server information.
    .Keep error response formats consistent.
    .Return field-specific validation errors whenever possible.
    .Log server-side errors for debugging.
    .Provide enough information for clients to fix the request without revealing internal implementation details.

