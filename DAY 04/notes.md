1. What is Django and why is it used?
-Django is a Python web framework used to build websites, APIs, and backend applications quickly
  .Why use it?
   ->Built-in authentication
   ->Database support
   ->URL routing
   ->Admin panel
   ->Security features
   ->Saves development time
Easy understanding:
Think of Django as a fully furnished house. Instead of building walls, doors, and plumbing yourself, everything is already provided and you just customize it.

2. What is the difference between a Django Project and a Django App?

    Django Project                           Django App

.Complete website/application              .A module performing one task
.Contains settings and configurations      .Contains specific functionality
.One project can have many apps            .App can be reused in other projects

Simple Analogy
Project = the whole shopping mall
Apps = individual stores inside the mall

A single Django project can contain many apps.

3. Understanding Django's "batteries-included" approach 
"In Django, the term "batteries included" means that the framework comes with a wide range of built‑in features and tools so you can build fully functional web applications without having to install many third‑party packages."

-Django provides many features by default.

  Examples:

  .Login system
  .Admin panel
  .ORM (database handling)
  .Security protection
  .Session management

So developers don't need to code these from scratch

4. Basic Django Project Structure:
 -> manage.py
    Command-line utility for managing Django projects.
    Examples:
    python manage.py runserver
    python manage.py startapp core

    Purpose:
     .Run server
     .Create apps
     .Apply migrations
     .Create admin users

->Project Folder
  Contains project configuration files.
  Example:
   backend_journey/

->settings.py
  Stores project settings.
  Examples:
  .Installed apps
  .Database configuration
  .Time zone
  .Security settings

->urls.py
  Maps URLs to views.
  Example:
  path('', views.home)

 When user visits /, Django calls home().

5. What is a Development Server? 
A lightweight server used for testing during development.
Run it using:
   python manage.py runserver

output:
   Starting development server at
   http://127.0.0.1:8000/

6. How Browser Communicates with Django:
   Step 1:
   Browser sends request
      GET /

   Step 2:
   Django checks urls.py

   Step 3:
   Matching view function is found

   Step 4
   View processes request

   Step 5
   Response is returned

   Step 6
   Browser displays response


-Django is a Python web framework used for backend development.
-Advantages: Fast development, security, admin panel, ORM, scalability.
-Project: Complete application; App: Specific functionality.
-manage.py: Executes Django commands.
-settings.py: Stores project configurations.
-urls.py: Maps URLs to views.
-Views handle requests and generate responses.
-Django handles requests by URL matching → View execution → Response generation


Mini Reflection Answers
->>Why use Django instead of writing everything from scratch?
  Because Django already provides authentication, database handling, security, admin panel, and URL routing, saving a lot of development time.

-->Difference between Project and App?
   .Project: Entire website/application.
   .App: A component handling one specific feature.

-->What happens internally when visiting a URL?
   .Browser sends request.
   .Django checks urls.py.
   .Matching view is found.
   .View executes.
   .Response is returned.
   .Browser displays the result.

-->Which part felt most similar to APIs studied earlier?

 The view function.

Just like APIs, a Django view:
   .Receives an HTTP request
   .Processes data
   .Returns an HTTP response