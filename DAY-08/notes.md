
1. What is an API? 
   An API (Application Programming Interface) allows different software applications to communicate and exchange data.

2. Why do we need Django REST Framework (DRF)?
   DRF helps developers build APIs easily by providing tools for serialization, authentication, permissions, and handling requests/responses.

3. Difference between a Django View and an API View.
     Django View                      API View
   .Returns HTML pages              .Returns data (usually JSON)
   .Used for websites               .Used for APIs and mobile/web apps
   .Uses templates                  .Uses serializers

4. What is Serialization?
   Serialization is the process of converting Python objects into formats like JSON so they can be sent over the internet.

5. What is JSON Response?
   A JSON Response is data sent by an API in JSON (JavaScript Object Notation) format.

   Example:
   {
      "name": "Harshita",
      "course": "Django"
   }

6. Request → Process → Response Cycle in APIs
   .Client sends a Request.
   .Server Processes the request.
   .Server sends back a Response (usually JSON).
7. Real-world Examples of REST APIs
   📱 Instagram API – Fetch posts and user data.
   🛒 Amazon API – Manage products and orders.
   🎬 Netflix API – Retrieve movie and show details.
  🌤️ Weather API – Get current weather information.

8. Why do modern applications rely heavily on APIs?
   Modern applications use APIs because they allow different systems, websites, and mobile apps to communicate and share data efficiently.

9. How is an API response different from a web page response?
  An API response returns raw data (usually in JSON format) that is meant to be processed by applications, while a web page response returns HTML content that is meant to be displayed and interacted with by users in a browser.

  .API Response (JSON)
  {
    "name": "Harshita",
    "course": "Django"
  }
  .Web Page Response (HTML)
    <h1>Harshita</h1>
    <p>Course: Django</p>

Practice 
 1. Install and Configure Django REST Framework
    
   -Approach
     .Activated the virtual environment.
     .Installed Django REST Framework using pip install djangorestframework.
     .Added 'rest_framework' to the INSTALLED_APPS list in settings.py.
     .Started the Django development server using python manage.py runserver.
     .Verified that the server ran successfully without any errors.

   -Output
     .Django server started successfully.
     .The terminal displayed:
     .Starting development server at http://127.0.0.1:8000/
     .Opening http://127.0.0.1:8000/ in a browser showed the Django welcome page (or project home page).

 2. Create Your First API Endpoint.
   Approach:
    . Imported APIView and Response in views.py.
    .Created HelloAPIView with a get() method returning a JSON message.
    .Added the URL path /api/hello/ in urls.py.
    .Ran the server and accessed the endpoint.

   Output
     .Visiting http://127.0.0.1:8000/api/hello/ returns:

   {
     "message": "Hello from Django REST Framework!"
   }

   API vs Template Responses
   .API Response: Returns data in JSON format for applications.
   .Template Response: Returns rendered HTML pages for users in a browser.

 3. Create a Student API Using the Student model created
   Approach:
    .Created a StudentSerializer for the Student model.
    .Created StudentAPIView to fetch and serialize all student records.
    .Added the /api/students/ endpoint in urls.py and ran the server.

   Output:

   Visiting http://127.0.0.1:8000/api/students/ returns student data in JSON format, for example:

  [
    {
      "name": "Rahul",
      "email": "rahul@gmail.com",
      "age": 21,
      "course": "AI"
    }
  ]
   Why APIs Commonly Return JSON
   -JSON is lightweight and easy to read.
   -It is supported by most programming languages.
   -It enables efficient data exchange between applications.
 