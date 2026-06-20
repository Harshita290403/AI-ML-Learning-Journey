1. What are Views in Django?
  Views are Python functions or classes that receive a request and return a response.

  e.g.:
  from django.http import HttpResponse

  def home(request):
      return HttpResponse("Hello World")

2. Function-Based Views (FBVs)
   FBVs are normal Python functions used as views.

   e.g.:
   def about(request):
       return HttpResponse("About Page")

3. URL Routing and how Django maps URLs to Views?
   In Django, URL routing decides which view should handle a user's request.

   Step 1: User Requests a URL
     A user enters a URL in the browser:
     http://127.0.0.1:8000/about/

   Step 2: Django Checks urls.py
    Django looks at the project's urls.py file and matches the requested path.

   Step 3: Django Calls the View
    If the URL matches, Django runs the corresponding view.

   Step 4: Django Sends a Response
    The view returns a response, which Django sends back to the browser.
     Browser displays:- This is the About page

    Request Flow:
    Browser
      ↓
    Requested URL (/about/)
      ↓
    urls.py
      ↓
    View Function (about)
      ↓
    Response
      ↓
    Browser

4.  What are Templates? 
    Templates are HTML files used to display web pages.
    e.g.: <h1>Welcome</h1>

5. Why Templates are used in web applications?
   Templates separate design (HTML) from logic (Python).

   Benefits of seperating logic with presentation:
   .Cleaner code
   .Easy to edit UI
   .Dynamic content support

6. What is Context?
   Context is a Python dictionary used to send data from a View to a Template.

   Request Flow with Context:
   Browser
      ↓
    URL
      ↓
    View
      ↓
    Context (dictionary with data)
      ↓
    Template
      ↓
    Rendered HTML
      ↓
    Browser

7. How is django seperating business logic from presentation?
  Django follows the MTV (Model–Template–View) architecture, which keeps application logic separate from the user interface.

  1. Business Logic → Views (and Models)
      Business logic includes tasks such as:
       .Fetching data from the database
       .Processing user input
       .Performing calculations
       .Applying rules and validations

       Example (views.py)

  2. Presentation → Templates
      Templates are responsible only for displaying data. They contain HTML and simple template tags.

      Example (home.html)