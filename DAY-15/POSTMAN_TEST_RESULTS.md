# Postman Test Results

| Endpoint                       | Method | Status Code | Result | Notes                 |
|--------------------------------|--------|-------------|--------|-----------------------|
| /api/token/                    | POST   |    200      | Pass   | JWT generated         |
| /api/students/                 | GET    |    200      | Pass   | Student list returned |
| /api/students/                 | POST   |    201      | Pass   | Student created       |
| /api/students/1/               | GET    |    200      | Pass   | Student retrieved     |
| /api/students/1/               | PUT    |    200      | Pass   | Updated successfully  |
| /api/students/1/               | DELETE |    204      | Pass   | Deleted successfully  |
| /api/students/?search=Harshita | GET    |    200      | Pass   | Search working        |
| /api/students/?course=AI       | GET    |    200      | Pass   | Filter working        |
| /api/students/?ordering=age    | GET    |    200      | Pass   | Ordering working      |
| Invalid JWT                    | GET    |    401      | Pass   | Unauthorized          |
| No JWT                         | GET    |    401      | Pass   | Unauthorized          |
| Student ID 999                 | GET    |    404      | Pass   | Not Found             |
| Missing Name                   | POST   |    400      | Pass   | Validation Error      |

