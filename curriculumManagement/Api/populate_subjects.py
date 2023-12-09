import requests
import os
from dotenv import load_dotenv
from faker import Faker
from faker.providers import BaseProvider
from pprint import pprint
import random

load_dotenv()

fake = Faker()

# TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyMTM3NTgyLCJpYXQiOjE3MDIxMzAzODIsImp0aSI6Ijc1NDUyOGI2MThhYTRiYzU5MTQyNTgxNjNhMmIwYmVmIiwidXNlcl9pZCI6IjAyNTg5YTZiLWVkZGEtNDMwNi1hOWZiLTNiMDZmMDY4YzZjNSJ9.vtccLPRQgOMVllDTUfZXrhIUR3suKResanqhGBze080"
TOKEN = os.environ.get('TOKEN')
api_url = "http://127.0.0.1:8000/api/subjects/"
authorization = f"Bearer {TOKEN}"
num_fake_data = 2

teachers = ['0568572e-870d-435d-9a2d-8b5e8aff0d28', '1113d1db-6454-4dd9-91f6-f62186827009', '12d0cf17-58a0-4136-b790-141651e5ba9a', '14eea4c7-a8f8-473e-ac3d-10f09c3bd490', '191a6f74-84af-43bb-9442-edeace39971d', '1c01bbfa-198b-4996-afc0-1ff2708a5516', '21483875-e1b9-4151-8c1a-ffc914c661a2', '46afb857-2ea9-401a-b642-3d32d9fcda9a', '5be601b9-dcf9-4bf8-9c15-0eace21a7090', '6aa2acd6-904d-447c-9e31-a744aed517ef',
            '7fc579ea-7bab-4976-a42b-bf6952051adf', '87995ec7-3f6e-41b3-b971-d989dfaa41e2', '9490d6ce-0059-4603-b736-444d1b0ab83e', '9d1e10f2-2c37-4232-b6cd-f4cd5aa84c9f', 'a5b5023c-37e8-4469-b0a7-3bfa1b2add04', 'a5eb4008-34c1-4929-89ac-ab4bcb9bb4e2', 'dce2aaa0-67e7-4cf6-99ca-3f34466d8cb8', 'dd7c8f86-d1b0-45a5-a900-b868c7793979', 'def4ec43-a1f5-40ef-bcf4-cd33ae08c2f0', 'ff61f8a6-6616-46e5-8943-885565524a98']

classes = ['049943eb-63ee-412d-ac87-c97677b84be3', '2648dc33-c2c8-4dee-8146-2f01aa3e33aa', '2d3db1a2-3b32-4bac-ab84-214575f6fb94', '3e0820a5-5235-4f4b-a4fc-5607ca17a73c', '4a02b9c4-7c99-41ca-8470-28d1cf9cf67a', '6f67ec02-d5dc-4ed7-99ff-62aa0e3e2116',
           '7acffddc-ec2a-4fe9-be57-2f69628b5291', '9a76b188-b26b-42f2-ba1e-40f6342efecd', 'b2e0112c-cabf-4269-a021-135f00a63d28', 'c00525c1-0293-454a-8bd1-f31a40a1097f', 'c7241506-b4d0-454e-8cf8-b6302a9ea2a7', 'de09f2a2-97f2-4dc2-a170-70302f95f509']

subjects = ["Mathematics", "English Language/Literature", "Science (Physics, Chemistry, Biology)", "History", "Geography", "Computer Science", "Physical Education",
            "Economics", "Foreign Language (Spanish, French, etc.)", "Art", "Music", "Civics/Government", "Environmental Studies", "Business Studies", "Health Education"]


for grade in range(0, len(subjects)):
    teachersList = random.sample(teachers, 2)
    name = subjects[grade]
    subject_code = fake.unique.random_int(min=100, max=999)

    payload = {"teachers": teachersList, "name": name,
               "code": subject_code, "class_associated": random.choice(classes)}

    headers = {"Authorization": authorization,
               "Content-Type": "application/json"}

    response = requests.post(api_url, json=payload, headers=headers)

    print(response.json())

    if response.status_code == 201 or response.status_code == 200:
        print(f"Inserted: {name}")
    else:
        print(f"Failed to insert: {name}")
print("Done populating the database with fake classes.")
