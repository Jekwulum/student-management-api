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

teachers = ['cf5d0010c3c0449dadc1c6a7b8c48e4c', 'c00e92229efa4c2f85fcd0ae9a41a024', 'ca159189f95b4a3999b0cf336911b82f', '406e2402f5d041bd887d61ffdcdb6a4b', '276da2ff8b1e4fd4b8ebd63e53b91d37',
            '13ec2c84a4c84b5cbd0479a94860edb7', '735c5e0a88454abbbea0e2f9d0dfd619', 'd8905847358847709d5cee0644971548', '4349158fe7f2481cae8d84ff60554eba', '7d66eb4d3ee348d992c1eff8f8c242e1']

classes = ['8dab058ae43b46d0a5c4f9d3779e49fa', '9a47aeb972b645079e175bd0534bff84', 'c36f94e98bef4f40b09fed7466e1252c', '7cd4b7ba2499421d84ec3e5c4900430e', '8bf1deb7b4d945a198f2fb67a9f918f4',
           'f25781acb8f647bd9e4ac92d8c7ebada', '88c58a5779214c3585d840bcbeddf8f3', '2417ca199e3342b7b1839e3ebf933ea5', '6e857224254c4a908b4d1f3c963c8b6b', 'ca8967eda4d54e65b06e90c0daac36ac']

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
