1. What are Permissions in Django REST Framework?
   Permissions determine what an authenticated user is allowed to do with an API.

   They are checked after authentication and decide whether a user can:
    -View data
    -Create data
    -Update data
    -Delete data

    Example:
    .User logs in successfully (Authentication)
    .Permission checks whether the user can access /students/ (Authorization)

2. Authentication vs Permissions

   Authentication              Permissions
Verifies who the user is     Determines what the user can do
Checks identity	             Checks access rights
Happens first	             Happens after authentication
Example: JWT Token	         Example: IsAuthenticated

 Example:
  .JWT confirms the user is Harshita.
  .Permission decides if Harshita can delete a student.

3. Built-in Permission Classes
   1.AllowAny: .Allows everyone to access the API.
               .Authentication is not required.
        permission_classes = [AllowAny]

    2.IsAuthenticated: Only logged-in users can access the API.
       permission_classes = [IsAuthenticated]

    3.IsAdminUser: Only admin users (is_staff=True) can access.
       permission_classes = [IsAdminUser]

    4.IsAuthenticatedOrReadOnly: .Anyone can read data.
                                 .Only authenticated users can create, update, or delete.
       permission_classes = [IsAuthenticatedOrReadOnly]
    
4. Introduction to Filtering and Searching
   Filtering and searching help users retrieve only the data they need instead of fetching all records
   Without filtering: GET /students/
    Returns all students.

   With filtering: GET /students/?course=AI
    Returns only AI students.

5. Why Filtering and Searching Improve API Usability
  Benefits:
   .Faster data retrieval
   .Reduces unnecessary data transfer
   .Improves user experience
   .Makes APIs more flexible
   .Saves bandwidth and processing time

6. Why are Permissions Important Even After Authentication?
   Authentication only confirms who the user is.
   
   Permissions determine what actions that user is allowed to perform.
   Example:
    .Both a student and an admin can log in.
    .Only the admin should be able to delete student records.

   Without permissions, every authenticated user could access sensitive operations.

7. Difference Between Searching and Filtering
| Filtering             |      Searching                       |
| --------------------- | ------------------------------------ |
| Finds exact matches   | Finds partial matches using keywords |
| Based on field values | Based on text search                 |
| Example: course=AI    | Example: search=har                  |

 Examples:
  Filtering
    GET /students/?course=AI

  Searching
    GET /students/?search=Har

  Returns:
   .Harshita
   .Harsh
   .Hari

8. Real-World Examples of Filtering and Ordering
1.Amazon
    .Filter by price
    .Brand
    .Rating
    .Category

    Ordering:
    .Price Low to High
    .Best Selling
    .Newest First
    .Flipkart

2.Filters:
    .RAM
    .Storage
    .Brand
    .Color

    Sorting:
    .Popularity
    .Price
    .Customer Rating

3.YouTube

   Search:
    .Python Django

  Filters:
   .Upload Date
   .Duration
   .Channel

  Sorting:
  .Relevance
  .Upload Date
  .View Count

4.LinkedIn

Filters:

Location
Experience
Company
Skills

Sorting:

Most Relevant
Most Recent

9. Which Permission Class Would You Use for a Public Blog API?
  The best choice is:
    IsAuthenticatedOrReadOnly

  Reason:
   .Anyone can read blog posts.
   .Only authenticated users can create, edit, or delete posts.

10. SearchFilter
    SearchFilter is a DRF filter backend that allows users to search across specified text fields using keywords.

    Enable SearchFilter
      from rest_framework import filters

    class StudentListAPIView(ListAPIView):
       queryset = Student.objects.all()
       serializer_class = StudentSerializer

       filter_backends = [filters.SearchFilter]
       search_fields = ['name', 'course']