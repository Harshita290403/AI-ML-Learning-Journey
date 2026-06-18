import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

users = response.json()

for user in users:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("Company:", user["company"]["name"])
    print()

print("Total Users:", len(users))

# Approach
# Send GET request.
# Convert response to JSON.
# Loop through users.
# Print required details.
# Count users using len().

# OUTPUT:
# Name: Leanne Graham
# Email: Sincere@april.biz
# Company: Romaguera-Crona


# Name: Ervin Howell
# Email: Shanna@melissa.tv
# Company: Deckow-Crist


# ...


# Total Users: 10


# How APIs help backend systems?
# APIs allow different services to communicate.
# Examples:
# Payment service talks to bank servers.
# Food delivery app communicates with restaurant systems.
# Login system communicates with authentication servers.
