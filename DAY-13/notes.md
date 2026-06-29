Study: 
- What is JWT (JSON Web Token)? 
- Difference between Token Authentication and JWT Authentication 
- Structure of a JWT: 
- Header 
- Payload 
- Signature 
- Access Token vs Refresh Token 
- Why JWT is widely used in modern web and mobile applications

Answer the following in your notes: 
- Why is JWT more commonly used than basic Token Authentication? 
- What is the purpose of a Refresh Token? 
- Why should Access Tokens have a short expiry time? 
- Which authentication method would you choose for a production application and why?

"notes.md" should contain: 
- What is JWT? 
- Structure of a JWT. 
- Access Token vs Refresh Token. 
- Token Authentication vs JWT Authentication. 
- Advantages of JWT. 
- Best practices for securing APIs.

1. JWT (JSON Web Token)
   JWT (JSON Web Token) is a compact, secure, and self-contained way to transmit information between two parties as a JSON object. It is commonly used for authentication and authorization in web and mobile applications.

   When a user logs in successfully:

  -The server verifies the user's credentials.
  -The server generates a JWT.
  -The client stores the JWT (usually in secure storage).
  -The client sends the JWT with each API request.
  -The server verifies the JWT before allowing access.

2. Difference between Token Authentication and JWT Authentication
     Token Authentication	                                     JWT Authentication
Uses a random token stored on the server.	                 Uses a signed JSON token containing user information.
Server must store tokens in a database.	                   Server usually does not need to store tokens (stateless).
Every request requires checking the database.	             Server verifies the token signature without database lookup (in many implementations).
Simpler to implement.                                      More scalable and widely used.
Suitable for small projects.	                             Suitable for large web and mobile applications.

3. Structure of a JWT
   A JWT consists of three parts separated by dots (.): Header.Payload.Signature
  
  -Header
   The Header contains metadata about the token.
    Example:
    {
     "alg": "HS256",
     "typ": "JWT"
    }

  -Payload
   The Payload contains the claims (information).
    Example:
    {
     "user_id": 15,
     "username": "harshita",
     "exp": 1750000000
    }

  -Signature
   The Signature ensures that the token has not been modified.
   It is created using:
     HMACSHA256(
       base64UrlEncode(header) +
      "." +
      base64UrlEncode(payload),
      secret_key
    )
   If anyone changes the payload, the signature becomes invalid.

4. Access Token vs Refresh Token
  Access Token	                                  Refresh Token
Used to access protected APIs.	             Used to generate a new Access Token.
Short lifespan (minutes).	                   Longer lifespan (days or weeks).
Sent with every API request.	               Used only when the Access Token expires.
If stolen, attacker gets temporary access.	 Must be stored securely because it can issue new Access Tokens.

5. Why JWT is widely used in modern web and mobile applications
   JWT is popular because it:
    -Is stateless, reducing server-side storage.
    -Scales well for large applications.
    -Works across different platforms and programming languages.
    -Supports secure authentication using digital signatures.
    -Is easy to use with REST APIs.
    -Is suitable for Single Page Applications (SPAs) and mobile apps.

6. What is the purpose of a Refresh Token?
   A Refresh Token allows the client to obtain a new Access Token after the current one expires without requiring the user to log in again.

7. Why should Access Tokens have a short expiry time?
  Access Tokens should expire quickly because:
   -If an attacker steals the token, it can only be used for a limited time.
   -It reduces the impact of token leakage.
   -It encourages periodic revalidation using Refresh Tokens.
   -It improves overall application security.
  Typical expiry:
   .Access Token: 5–30 minutes
   .Refresh Token: Several days or weeks

8. Which authentication method would you choose for a production application and why?
  For a production application, JWT Authentication is generally the better choice.

  