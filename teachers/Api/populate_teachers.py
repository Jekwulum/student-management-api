import requests
from faker import Faker
from faker.providers import BaseProvider
from pprint import pprint
import random

fake = Faker()

USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5MTM0Mzc3LCJpYXQiOjE2OTkxMjcxNzcsImp0aSI6IjFiYWUzYjlhNzVlODQ4MzU4YzczYjM4OWMxOTNkMGU3IiwidXNlcl9pZCI6ImZmNWNhMmRhLTBlY2QtNGNjOC1hMjdmLTRjZmU2MjFlMzE1OSJ9.y3DcUYS_Hj6B0x9ZtEU9x4nWtXGoB3JgRGAfqbEvO-g"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyMTE1MjY5LCJpYXQiOjE3MDIxMDgwNjksImp0aSI6IjM5ZjkyYjQzMTc2NjQ3ZTE4YjBhZjQxNTlkOTkwODc1IiwidXNlcl9pZCI6IjAyNTg5YTZiLWVkZGEtNDMwNi1hOWZiLTNiMDZmMDY4YzZjNSJ9.FuSDFpmwBzLR53DnYgnY2bnTgsdaUnj10hA07nm8tOA"
api_url = "http://127.0.0.1:8000/api/teachers/"
authorization = f"Bearer {TOKEN}"

num_fake_data = 5

existing_teachers = ['6fde1d89-e4cd-4a97-b0e9-054380e8a786', '587f7a2b-6683-4f5c-9ab0-386d5f01f84a', 'b5944e6d-8add-4ae2-b1b7-5bf90d170053', 'e2b1e6a8-57a1-480e-8cbb-8e805cfdd132', 'a474dc80-62c9-404a-8ad5-eb616a4501d7',
                     'f07597f5-d6f6-429d-803c-64ea2067e0e1', '49d18d11-7209-43b6-87f7-7feacf2fefc6', '0b8a9847-86af-41e7-bf5d-ea19c62fa639', '78b6ef98-0989-464b-a4d6-0072d5145b92', '0378b615-6e1d-4fe4-8d07-816fa0a8a3c1']

for _ in range(num_fake_data):
    first_name = fake.first_name()
    last_name = fake.last_name()
    user = random.choice(existing_teachers)
    payload = {"user": user}

    headers = {"Authorization": authorization,
               "Content-Type": "application/json"}

    response = requests.post(api_url, json=payload, headers=headers)

    pprint(response.json())

    if response.status_code == 201 or response.status_code == 200:
        print(f"Inserted: {first_name} {last_name}")
        # user_ids.append(response.data.user_id)
    else:
        print(f"Failed to insert: {first_name} {last_name} {user}")
print("Done populating the database with fake names.")
