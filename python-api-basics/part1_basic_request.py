"""
Part 1: Basic GET Request
=========================
Difficulty: Beginner

Learn: How to make a simple GET request and view the response.

We'll use JSONPlaceholder - a free fake API for testing.
"""
#Ex-1

import requests
'''
# Step 1: Define the API URL
url = "https://jsonplaceholder.typicode.com/posts/5"

# Step 2: Make a GET request
response = requests.get(url)

# Step 3: Print the response
print("=== Basic API Request ===\n")
print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"\nResponse Data:")
print(response.json())

#Ex-2 

# Step 1: Define the API URL
url = "https://jsonplaceholder.typicode.com/users"

# Step 2: Make a GET request
response = requests.get(url)

# Step 3: Print the response
print("=== Fetch All Users ===\n")
print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"\nResponse Data:")
print(response.json())'''

# Ex-3

# Step 1: Define the API URL
url = "https://jsonplaceholder.typicode.com/posts/999"

# Step 2: Make a GET request
response = requests.get(url)

# Step 3: Print the response
print("=== Fetch All Users ===\n")
print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"\nResponse Data:")
print(response.json())
if response.status_code == 404:
    print("\nPost not found!")

# --- EXERCISES ---
# Try these on your own:
#
# Exercise 1: Change the URL to fetch post number 5
#             Hint: Change /posts/1 to /posts/5
#
# Exercise 2: Fetch a list of all users
#             URL: https://jsonplaceholder.typicode.com/users
#
# Exercise 3: What happens if you fetch a post that doesn't exist?
#             Try: https://jsonplaceholder.typicode.com/posts/999
