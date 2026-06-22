1. What is CRUD? 
- Create 
- Read 
- Update 
- Delete 

  CRUD stands for the four basic operations performed on data in a database.
  Simple Analogy: A Notebook
   .Create → Write a new entry in the notebook.
   .Read → Read an existing entry.
   .Update → Edit or correct an entry.
   .Delete → Erase an entry.

2. How Django ORM simplifies database operations ?
   Django ORM (Object Relational Mapper) allows you to interact with a database using Python code instead of SQL queries.

3. Difference between SQL queries and ORM queries.
   Feature	            SQL Queries	                 ORM Queries

Language Used	        SQL	                         Python

Complexity           	More verbose    	         Simpler and more readable

Database Dependency	   May need changes for          Works with multiple databases
                       different databases	         without code changes

Security	           Prone to SQL injection        Built-in protection
                       if not handled properly	     against SQL injection

Learning Curve	       Requires SQL knowledge	     Easier for Python developers

Query Execution	       Written manually	             Generated automatically by Django

4. Common ORM Methods: 
- "create()" 
- "all()" 
- "get()" 
- "filter()" 
- "save()" 
- "delete()" 

   1. create()
     Used to create and save a new record in the database in a single step.
    Syntax:
     ModelName.objects.create(field1=value1, field2=value2)
    E.g.: Student.objects.create(name="Harshita", age=20)
   
   2. all()
     Used to retrieve all records from a model.
    Syntax:
     ModelName.objects.all()
    Example: students = Student.objects.all()
   Returns a queryset containing all student records.

   3. get()
     Used to retrieve a single record that matches the given condition.
    Syntax
     ModelName.objects.get(condition)
    Example: student = Student.objects.get(id=1)

    4. filter()
     Used to retrieve multiple records that satisfy a condition.
    Syntax
     ModelName.objects.filter(condition)
    Example: students = Student.objects.filter(age=20)
   Returns a queryset containing all students whose age is 20.
   
   5. save()
     Used to save changes made to an existing object.
     Example:
      student = Student.objects.get(id=1)
      student.age = 21
      student.save()

    Updates the student's age in the database.

    6. delete()
     Used to remove a record from the database.
    Example:
     student = Student.objects.get(id=1)
     student.delete()
    Deletes the student record with id=1.

5. Why CRUD Forms the Foundation of APIs?
   CRUD forms the foundation of APIs because most applications need to manage data by creating, retrieving, updating, and deleting records.

   An API acts as a bridge between clients (such as web or mobile applications) and a database. Nearly every API endpoint performs one of the CRUD operations.

6. Which ORM operation felt the easiest to understand?
   The all() method felt the easiest to understand because it simply retrieves all records from the database with a single, readable command:
   
   Student.objects.all()

7. How would these operations be exposed through APIs in the future?
   These ORM operations are typically exposed through API endpoints using HTTP methods.