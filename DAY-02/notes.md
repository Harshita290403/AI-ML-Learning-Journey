1. What are Functions in Python and Why Are They Important in Backend Development?

FUNCTIONS: block of code that can be reused whenever needed
eg: def greet():
    print("Hello")

IMPORTANCE IN BACKEND:
.makes code reuseable
.reduce reptition of code and making it write again  and again 
.easy readablity and maintainance
.Helps organize API logic into smaller modules

2. Function Parameters and Return Values.

Parameters: Parameters are values passed into a function.

for e.g.:
def greet(name):
    print("Hello", name) "here name is the parameter"

greet("Harshita") 

Return Values: A function can send a result back using return.

for e.g.: 
def add(a, b):
    return a + b

result = add(5, 3)
print(result) #o/p = 8

3. Difference Between Local and Global Variables.

Local Variable: Declared inside a function and accessible only within that function.
for e.g.:
def test():
    x = 10
    print(x)

test()

Global Variable: Declared outside a function and accessible throughout the program.
for e.g.:
x = 20

def test():
    print(x)

test()

4. Reading from and Writing to Files in Python.

Writing to a File:

with open("data.txt", "w") as file:
    file.write("Hello World")

Reading from a File:

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

5. Exception Handling Using try-except.

Exception handling prevents a program from crashing when an error occurs.

for e.g.:

try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

Benefits:
.Handles errors
.Prevents application crashes.

6. Why APIs Need Clean Functions and Proper Error Handling.

. Clean Functions Improve Code Quality
e.g.:
def calculate_total(price, quantity):
    return price * quantity

This function has a single responsibility: calculating the total cost.

. Proper Error Handling Prevents API Failures

APIs interact with users, databases, and external services. Errors can occur at any time, such as:

Invalid user input
Missing files
Database connection issues
Network failures

Using try-except helps handle these errors gracefully instead of crashing the application.

-->>Why APIs Need It:

Prevents server crashes.
Returns meaningful error messages.
Improves reliability and security.
Helps users and developers identify issues quickly.

