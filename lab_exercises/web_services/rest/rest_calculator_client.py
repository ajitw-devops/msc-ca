import requests

# Base URL
base_url = "http://127.0.0.1:5001"

# Test addition
add_response = requests.post(
    f"{base_url}/add",
    json={"intA": 10, "intB": 20}
)
print("Addition Result:", add_response.json())

# Test subtraction
subtract_response = requests.post(
    f"{base_url}/subtract",
    json={"intA": 20, "intB": 10}
)
print("Subtraction Result:", subtract_response.json())
