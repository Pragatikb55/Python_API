import requests

# Step 1: Define the API URL
url = "https://jsonplaceholder.typicode.com/users"

# Step 2: Make a GET request
response = requests.get(url)

# Step 3: Print the response
print("=== Fetch All Users ===\n")
print(f"URL: {url}")
print(f"Status Code: {response.status_code}")
print(f"\nResponse Data:")
print(response.json())
