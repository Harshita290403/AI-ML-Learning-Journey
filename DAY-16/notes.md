1. Why shouldn't passwords be stored directly in the database?
   Passwords should never be stored directly because if the database is hacked, attackers can see every user's password. Instead, passwords are stored as hashed values, making them unreadable. This protects user accounts even if the database is compromised.

2. Why do applications separate registration and login?
   Registration and login serve different purposes.
     -Registration creates a new user account and stores user details securely.
     -Login verifies an existing user's credentials and grants access.
   Keeping them separate makes authentication more secure, organized, and easier to manage.

3. How does request.user simplify backend development?
   request.user provides the currently authenticated user for every request.
   It allows developers to:
   -Identify who is making the request.
   -Show only that user's data.
   -Restrict access to authorized users.
   -Avoid manually checking user information in every view.

4. Why do applications have User Authentication?
   User authentication ensures that only authorized users can access protected resources.
   It helps to:
     -Protect sensitive data.
     -Verify user identity.
     -Prevent unauthorized access.
     -Provide personalized user experiences.
     -Manage permissions and roles.

5. Django's Built-in User Model
   Django provides a built-in User model in django.contrib.auth.models.User.
   It includes fields like:
    -Username
    -Password (hashed)
    -Email
    -First Name
    -Last Name
    -is_active
    -is_staff
    -is_superuser

   It also includes methods for:
    -Creating users
    -Authenticating users
    -Changing passwords
    -Managing permissions

6. Password Hashing
   Password hashing converts a password into a fixed-length encrypted value that cannot easily be reversed.
   ## Example:
    Password: MyPassword123
    Stored in database: pbkdf2_sha256$600000$...

  Django automatically hashes passwords using secure algorithms such as PBKDF2.
   Benefits:
   -Original password is not stored.
   -Difficult for attackers to recover passwords.
   -Improves overall security

7. Why passwords should never be stored in plain text
   Plain text passwords are dangerous because:
    -Anyone with database access can read them.
    -A database breach exposes every user's password.
    -Users often reuse passwords on multiple websites.
    -It violates security best practices.
   Using hashed passwords greatly reduces these risks.

8. Authentication Flow in Modern Applications
   --> User enters username/email and password.

   --> Client sends credentials to the server.
    
   --> Server checks if the user exists.
    
   --> Server compares the entered password with the stored hashed password.
    
   --> If valid, authentication succeeds.
    
   --> Server returns a session or JWT access token.
    
   --> User includes the token in future requests.
    
   --> Server verifies the token before allowing access to protected resources.

9. Registration Flow
   -User fills out the registration form.
   -Client sends user details to the backend.
   -Backend validates the input.
   -Password is hashed.
   -User record is saved in the database.
   -Registration success response is returned.
   -User can now log in.

10. Login Flow
    -User enters username/email and password.
    -Client sends credentials to the server.
    -Server verifies the credentials.
    -Password hash is compared with the stored hash.
    -If authentication succeeds:
       .A session or JWT token is generated.
       .The token is returned to the client.
    -Client stores the token.
    -Token is sent with future requests.
    -Backend verifies the token and grants access to protected resources.

11. Best Practices for User Authentication
    -Never store passwords in plain text.
    -Always hash passwords using secure algorithms.
    -Use HTTPS to encrypt data in transit.
    -Validate all user inputs.
    -Use strong password policies.
    -Use JWT or secure sessions for authentication.
    -Set token expiration times.
    -Protect sensitive endpoints with authentication.
    -Use permissions and roles to control access.
    -Log users out by invalidating sessions or tokens.
    -Keep authentication libraries and dependencies updated.
    -Enable rate limiting to reduce brute-force attacks.
    -Consider multi-factor authentication (MFA) for additional security.
