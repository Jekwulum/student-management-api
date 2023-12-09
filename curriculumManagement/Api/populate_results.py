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

teachers = ['0568572e-870d-435d-9a2d-8b5e8aff0d28', '1113d1db-6454-4dd9-91f6-f62186827009', '12d0cf17-58a0-4136-b790-141651e5ba9a', '14eea4c7-a8f8-473e-ac3d-10f09c3bd490', '191a6f74-84af-43bb-9442-edeace39971d', '1c01bbfa-198b-4996-afc0-1ff2708a5516', '21483875-e1b9-4151-8c1a-ffc914c661a2', '46afb857-2ea9-401a-b642-3d32d9fcda9a', '5be601b9-dcf9-4bf8-9c15-0eace21a7090', '6aa2acd6-904d-447c-9e31-a744aed517ef',
            '7fc579ea-7bab-4976-a42b-bf6952051adf', '87995ec7-3f6e-41b3-b971-d989dfaa41e2', '9490d6ce-0059-4603-b736-444d1b0ab83e', '9d1e10f2-2c37-4232-b6cd-f4cd5aa84c9f', 'a5b5023c-37e8-4469-b0a7-3bfa1b2add04', 'a5eb4008-34c1-4929-89ac-ab4bcb9bb4e2', 'dce2aaa0-67e7-4cf6-99ca-3f34466d8cb8', 'dd7c8f86-d1b0-45a5-a900-b868c7793979', 'def4ec43-a1f5-40ef-bcf4-cd33ae08c2f0', 'ff61f8a6-6616-46e5-8943-885565524a98']

subjects = ['01bc4434-2607-4681-9d5f-f85d7aaa32a6', '158f1c69-2248-4e8a-8426-86531aba1ad0', '24428de9-23ef-41fb-9fed-895a1c840381', '403af69d-76e9-4ab7-baaf-43c5d26940b8', '4f49eb5c-9d30-4799-84b5-92e658a544eb', '5aed7059-71b6-4381-8e3e-8079955ed917', '5d9d8dbd-8005-46b0-97b5-ef8287aefadb',
            '63441c86-6817-453e-b12b-db79afd74a7f', '92626d6f-19d6-4df7-94a7-0356157fccf4', '963b4f82-baa3-4ccd-b87d-a79c0830f2b6', 'a2cf325f-7f5d-426e-8be0-481a035e4be8', 'aad6649f-6468-45f5-80b5-a8ea3fcf444c', 'd79a3eea-7e2c-442e-a735-ed720c7a70e7', 'f5e1fd18-80ae-4752-a90d-3926805c97a7', 'fe34a4e4-ee13-4e8b-aad5-90ca5ce10a3b']

random_date = fake.date_this_year()

for idx in range(0, len(students)):
    date = str(random_date)

    payload = {
        "student": students[idx],
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
