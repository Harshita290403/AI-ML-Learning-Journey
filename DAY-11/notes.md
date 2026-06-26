1. Why Generic Views are used in Django REST Framework
  Generic Views are used to reduce repetitive code while creating APIs. They provide built-in functionality for common operations such as listing, creating, updating, retrieving, and deleting objects. This makes API development faster, cleaner, and easier to maintain.

2. Difference between APIView, GenericAPIView, and Concrete Generic Views
| Feature                  | APIView | GenericAPIView    | Concrete Generic Views |
| ------------------------ | ------- | ----------------- | ---------------------- |
| Built-in CRUD operations | ❌ No   | ❌ No            | ✅ Yes                 |
| Serializer support       | Manual  | Automatic support | Automatic support      |
| Queryset handling        | Manual  | Automatic support | Automatic support      |
| Code required            | More    | Moderate          | Least                  |
| Reusability              | Low     | Medium            | High                   |

APIView:
  .Base class for building custom APIs.
  .Developers write methods like get(), post(), put(), and delete() manually.

GenericAPIView:
  .Extends APIView.
  .Adds support for queryset, serializer_class, filtering, and pagination.
  .Still requires mixins or custom methods.

Concrete Generic Views:
  .Ready-made views combining GenericAPIView with mixins.
  .Perform CRUD operations with minimal code.

3. Understanding ListCreateAPIView
   ListCreateAPIView is used when an endpoint should:

  .GET → Return a list of objects.
  .POST → Create a new object.

  Example:
  class StudentListCreateView(ListCreateAPIView):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer


4. Understanding RetrieveUpdateDestroyAPIView

RetrieveUpdateDestroyAPIView is used when an endpoint should:

GET → Retrieve a single object.
PUT/PATCH → Update an object.
DELETE → Delete an object.

Example:

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

5. Benefits of Reusable Code in Backend Development
Reduces code duplication.
 -Improves readability.
 -Makes maintenance easier.
 -Decreases chances of bugs.
 -Speeds up development.
 -Encourages consistent API design.

6. How are Generic Views better than APIViews?
   Generic Views are better because they already provide common CRUD functionality. Developers only need to specify the queryset and serializer, whereas APIViews require writing each method manually.

7. Which Generic View did you use today?
   used:
   RetrieveUpdateDestroyAPIView

  for updating, retrieving, and deleting student records.
  (If you also created a list/create endpoint, then you additionally used ListCreateAPIView.)

8. Why should backend developers avoid writing repetitive code?
   Backend developers should avoid repetitive code because it:
    .Increases maintenance effort.
    .Makes projects harder to understand.
    .Introduces unnecessary bugs.
    .Slows down future development.
   Reusable components help keep the codebase clean and scalable.

9. Which part of today's task saved the most code?
   Using Concrete Generic Views, especially:
     .RetrieveUpdateDestroyAPIView
   saved the most code because it automatically handled GET, PUT, PATCH, and DELETE operations without writing separate methods.

10. APIView vs Generic Views

         APIView	                        Generic Views
     More manual coding	                  Minimal coding
     CRUD methods written manually	      CRUD methods already implemented
     Less reusable	                      Highly reusable
     Suitable for complex custom logic	  Suitable for standard CRUD APIs
     More flexible               	       Faster to develop

11. Benefits of Reusable Backend Code
     .Faster API development.
     .Cleaner project structure.
     .Easier debugging.
     .Better scalability.
     .Consistent implementation across endpoints.
     .Less repetitive code and improved productivity.