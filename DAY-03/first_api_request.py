import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Title:", data["title"])

print("Complete JSON:")
print(data)

# Approach
# Import requests.
# Send a GET request.
# Check status code.
# Convert response into JSON.
# Print title and full response.


# OUTPUT:
# Status Code: 200

# Title:
# sunt aut facere repellat provident occaecati excepturi optio reprehenderit

# Complete JSON:

# {
# 'id':1,
# 'userId':1,
# 'title':'sunt aut facere...',
# 'body':'quia et suscipit...'
# }

# Why GET is commonly used?
# GET requests are mainly used to retrieve information from a server without changing anything.
# Examples:
# Viewing products
# Reading blog posts
# Checking weather