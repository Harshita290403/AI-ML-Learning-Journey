1. What are Models in Django?
   Models are Python classes that define the structure of database tables.
   E.g.:
      class Student(models.Model):
         name = models.CharField(max_length=100)

2. Why do backend applications need databases? 
   Databases store data permanently and allow easy searching, updating, and deleting of records.

3. Introduction to SQLite
   SQLite is Django's default lightweight database stored in a file named db.sqlite3.

4. Understanding Django ORM (Object Relational Mapper) 
   ORM (Object Relational Mapper) lets us interact with the database using Python code instead of SQL.
   e.g.: Student.objects.create(name="John")

5. What are Migrations? and why are they needed? 
   Migrations convert model changes into database table changes.
   Migrations are needed because databases do not automatically understand changes made in Python model files.
   They help Django:
    .Create new tables
    .Add or remove columns
    .Modify existing fields
    .Delete tables
    .Keep the database structure synchronized with models

6. What is Django Admin and why is it powerful?
   Django Admin is a built-in web interface provided by Django that allows developers to manage application data through a browser.

   Django Admin Powerful:
   .Automatic Interface Generation
   .Easy Data Management
   .Authentication and Permissions
   .Customizable
   .Saves Development Time

7. Why do we use databases instead of text files?
   Databases store large amounts of data efficiently and support searching, updating, and multiple users.

8. What problem does Django ORM solve? 
   ORM removes the need to write SQL queries manually.

9. Why are migrations necessary? 
   They safely update the database whenever models change.

10. What impressed you most about Django Admin?
   It automatically provides a fully functional admin interface with almost no extra coding.

11. Advantages of Admin Panel in rapid development.
   Django Admin speeds up rapid development by providing a ready-made, secure interface to manage application data without building custom admin pages.
