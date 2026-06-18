1.What is an API and why is it used?
->API (Application Programming Interface) allows two applications to communicate with each other.
->API is used as it saves time and effort,data and feature integration,automation

2.Difference between Frontend and Backend
   Frontend	                 Backend
.What users see	       .Works behind the scenes
.HTML, CSS, JS	       .Python, Django, Database
.Buttons, forms	       .APIs, logic, data storage

3. What are HTTP Methods?
HTTP methods tells what operation to perform on on specific online resource and all according to standards.

Method	       Purpose	        Example
GET	           Read data	   View profile
POST	       Create data	   Register user
PUT	           Update data	   Edit profile
DELETE	       Remove data	   Delete account

4.What is JSON and why is it commonly used in APIs?
-> JSON (JavaScript Object Notation) is a lightweight format for exchanging data.
   {
  "name":"Harshita",
  "age":21
   }
->Why use JSON?
Easy to read
Lightweight
Supported by almost every programming language
Ideal for APIs

5.Introduction to Python's "requests" library
- It is 3rd party package used to send HTTP requests and interact with web resources and APIs
-INSTALLATION--pip install requests
-IMPORT-- import requests
-It helps Python communicate with APIs.

6.- Real-life examples of APIs (Weather Apps, Payment Gateways, Authentication Systems)
--WEATHER APP:
    .Request: app reads our smartphone gps coordinates and passes them to weather server
    .Processing: API locates  precise grid coordinates and fetch the matching radar and atmospheric data
    .Response: The server returns a lightweight data file(JSON format) containing temp.,wind speeds and rain forecast

--PAYMENT GATEWAYS:
    .GIve card info on payment form on e commerce store
    .the store transmits details with encrypted API call directly to stripe or paypal
    .Payment gateway's API securely commuicates with bank to verify
    .The API relays clean success or failure signal to online store
    .the online store shows changes to order confirmed

--AUTHENTICATION SYSYSTEMS:
   uses login with google helps in allowing users too securely verify their identity across third party applications without ever sharing their actual passwords