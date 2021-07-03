import requests

import json

url = "http://127.0.0.1:8000/api/user"

customer = {
    "name": "Ritik Kumar",
    "age": 21,
    "phone": "971957118987",
    "city": "Najibabad",
    "country": "India",
    "linkedin_profile": "http://www.ksksks.com"
}

for i in range(1, 3000):
    response = requests.post(url, json=customer)
    print(response.elapsed.total_seconds())
