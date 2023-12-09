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

TOKEN = os.environ.get('TOKEN')
api_url = "http://127.0.0.1:8000/api/attendance/"
authorization = f"Bearer {TOKEN}"
num_fake_data = 2

students = studentIds

classes = ['049943eb-63ee-412d-ac87-c97677b84be3', '2648dc33-c2c8-4dee-8146-2f01aa3e33aa', '2d3db1a2-3b32-4bac-ab84-214575f6fb94', '3e0820a5-5235-4f4b-a4fc-5607ca17a73c', '4a02b9c4-7c99-41ca-8470-28d1cf9cf67a', '6f67ec02-d5dc-4ed7-99ff-62aa0e3e2116',
           '7acffddc-ec2a-4fe9-be57-2f69628b5291', '9a76b188-b26b-42f2-ba1e-40f6342efecd', 'b2e0112c-cabf-4269-a021-135f00a63d28', 'c00525c1-0293-454a-8bd1-f31a40a1097f', 'c7241506-b4d0-454e-8cf8-b6302a9ea2a7', 'de09f2a2-97f2-4dc2-a170-70302f95f509']

random_date = fake.date_this_year()

for idx in range(0, len(students)):
    date = str(random_date)

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
