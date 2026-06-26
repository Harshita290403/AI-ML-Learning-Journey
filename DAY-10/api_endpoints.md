GET     /api/students/

GET     /api/student/<id>/

POST    /api/students/create/

PUT     /api/student/update/<id>/

PATCH   /api/student/update/<id>/

DELETE  /api/student/delete/<id>/


Sample POST Request

{
"name":"Ananya",
"email":"ananya@gmail.com",
"age":20,
"course":"AI"
}


Sample Response

{
"message":"Student created successfully"
}