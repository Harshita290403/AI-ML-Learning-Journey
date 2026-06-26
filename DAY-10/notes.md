1. What are CRUD APIs?
   CRUD stands for the four basic operations performed on data in an application.

Operation        	Meaning	                 Example
Create	         Add new data	            Add a new student
Read    	    Retrieve existing data  	View student details
Update	        Modify existing data	    Change a student's course
Delete	        Remove data	                Delete a student record

2. HTTP Methods
   HTTP methods tell the server what action the client wants to perform.

   GET- Used to retrieve data.
   POST- Used to create new data.
   PUT- Used to replace an entire resource
   PATCH- Used to partially update a resource.
   DELETE- Used to remove data.

3. Request Body and Response Body
   Request Body- The data sent from the client to the server.
   Response Body- The data sent from the server back to the client.

4. Status Codes
   Status codes tell the client whether the request succeeded or failed.
   200 OK -Request completed successfully.
   400 Bad Request- Client sent invalid data.
   404 Not Found- Requested resource does not exist.

5. How CRUD APIs Power Real-World Applications
   Almost every modern application is built using CRUD operations.
Social Media

Create → Post a photo

Read → View posts

Update → Edit caption

Delete → Remove post

6. Which CRUD operation was easiest?
   The Read (GET) operation was the easiest because it only retrieves and displays data without modifying the database.

7. Which operation requires the most caution in production?
   The Delete (DELETE) operation requires the most caution because it permanently removes data, which may be difficult or impossible to recover.

8. How does DRF simplify CRUD development?
   DRF simplifies CRUD development by providing:

   .Serializers for data validation and JSON conversion.
   .APIView and Generic Views to reduce boilerplate code.
   .Built-in status codes and responses for standardized API behavior.
   .Automatic request parsing and response rendering.
   .Reusable components that make APIs easier to maintain and scale.