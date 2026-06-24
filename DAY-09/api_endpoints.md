# API Endpoints


## /api/students/

Sample Response

[
  {
    "name":"Rahul",
    "email":"rahul@gmail.com",
    "age":21,
    "course":"AI"
  }
]



## /api/student/<id>/

Sample Response

{
   "name":"Rahul",
   "email":"rahul@gmail.com",
   "age":21,
   "course":"AI"
}



Error Response

{
   "error":"Student not found"
}