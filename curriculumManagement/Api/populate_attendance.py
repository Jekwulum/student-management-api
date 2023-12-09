import requests
import os
import random
from dotenv import load_dotenv
from faker import Faker
from faker.providers import BaseProvider
from pprint import pprint
from studentIds import studentIds

load_dotenv()

fake = Faker()

# TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyMTM3NTgyLCJpYXQiOjE3MDIxMzAzODIsImp0aSI6Ijc1NDUyOGI2MThhYTRiYzU5MTQyNTgxNjNhMmIwYmVmIiwidXNlcl9pZCI6IjAyNTg5YTZiLWVkZGEtNDMwNi1hOWZiLTNiMDZmMDY4YzZjNSJ9.vtccLPRQgOMVllDTUfZXrhIUR3suKResanqhGBze080"
TOKEN = os.environ.get('TOKEN')
api_url = "http://127.0.0.1:8000/api/attendance/"
authorization = f"Bearer {TOKEN}"
num_fake_data = 2

students = studentIds

classes = ['8dab058ae43b46d0a5c4f9d3779e49fa', '9a47aeb972b645079e175bd0534bff84', 'c36f94e98bef4f40b09fed7466e1252c', '7cd4b7ba2499421d84ec3e5c4900430e', '8bf1deb7b4d945a198f2fb67a9f918f4',
           'f25781acb8f647bd9e4ac92d8c7ebada', '88c58a5779214c3585d840bcbeddf8f3', '2417ca199e3342b7b1839e3ebf933ea5', '6e857224254c4a908b4d1f3c963c8b6b', 'ca8967eda4d54e65b06e90c0daac36ac']

random_date = fake.date_this_year()

for idx in range(0, len(students)):
    date = str(random_date)
    subject_code = fake.unique.random_int(min=100, max=999)

    payload = {
        "student": students[idx],
        "class_attended": random.choice(classes),
        "date": date,
        "is_present": random.choice([True, False])
    }
    print(payload)

    headers = {"Authorization": authorization,
               "Content-Type": "application/json"}

    response = requests.post(api_url, json=payload, headers=headers)

    print(response.json())

    if response.status_code == 201 or response.status_code == 200:
        print(f"Inserted: {date}")
    else:
        print(f"Failed to insert: {date}")
print("Done populating the database with fake classes.")
