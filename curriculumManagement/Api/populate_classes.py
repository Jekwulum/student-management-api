import requests
import os
from dotenv import load_dotenv
from faker import Faker
from faker.providers import BaseProvider
from pprint import pprint
import random

load_dotenv()

fake = Faker()

# TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyMTE3Mzg1LCJpYXQiOjE3MDIxMTAxODUsImp0aSI6IjcxZTU2Yjc0ZGJhMTRlN2FiOGJhMzU0NjQxNzUxZmY1IiwidXNlcl9pZCI6IjAyNTg5YTZiLWVkZGEtNDMwNi1hOWZiLTNiMDZmMDY4YzZjNSJ9.LKYS648STNoUou5HXvC5N0uOqmnb1yiFxgiJ6-rdcdk"
TOKEN = os.environ.get('TOKEN')
api_url = "http://127.0.0.1:8000/api/classes/"
authorization = f"Bearer {TOKEN}"

num_fake_data = 2

teachers = ['cf5d0010c3c0449dadc1c6a7b8c48e4c', 'c00e92229efa4c2f85fcd0ae9a41a024',
            'ca159189f95b4a3999b0cf336911b82f', '406e2402f5d041bd887d61ffdcdb6a4b', '276da2ff8b1e4fd4b8ebd63e53b91d37', '13ec2c84a4c84b5cbd0479a94860edb7',
            '735c5e0a88454abbbea0e2f9d0dfd619', 'd8905847358847709d5cee0644971548', '4349158fe7f2481cae8d84ff60554eba', '7d66eb4d3ee348d992c1eff8f8c242e1']

for grade in range(1, 13):  # Generate data for Grades 1 to 12
    teacher = random.choice(teachers)  # Select a random teacher
    class_name = f"Grade {grade}"
    class_code = fake.unique.random_int(min=100, max=999)

    payload = {"teacher": teacher, "name": class_name, "code": class_code}

    headers = {"Authorization": authorization,
               "Content-Type": "application/json"}

    response = requests.post(api_url, json=payload, headers=headers)

    print(response.json())

    if response.status_code == 201 or response.status_code == 200:
        print(f"Inserted: {class_name}")
    else:
        print(f"Failed to insert: {class_name}")
print("Done populating the database with fake classes.")
