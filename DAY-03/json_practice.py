import json

user = {
    "name": "Harshita",
    "email": "harshita@gmail.com",
    "age": 21,
    "skills": ["Python", "Machine Learning"]
}

json_data = json.dumps(user)

python_data = json.loads(json_data)

print("JSON Format:")
print(json_data)

print()

print("Python Dictionary:")
print(python_data)

# Approach
# Create a dictionary.
# Convert dictionary to JSON using dumps().
# Convert JSON back to dictionary using loads().
# Print both.

# OUTPUT:
# JSON Format:

# {"name":"Harshita",
# "email":"harshita@gmail.com",
# "age":21,
# "skills":["Python","Machine Learning"]}


# Python Dictionary:

# {
# 'name':'Harshita',
# 'email':'harshita@gmail.com',
# 'age':21,
# 'skills':['Python','Machine Learning']
# }

# Why JSON is the standard format?
# Human-readable
# Lightweight
# Fast data transfer
# Supported by all major languages
# Easy conversion between Python objects and JSON