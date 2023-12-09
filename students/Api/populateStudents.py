import requests
import os
from dotenv import load_dotenv
from faker import Faker
from faker.providers import BaseProvider

load_dotenv()

class SubjectProvider(BaseProvider):
    subjects = ["Mathematics", "Science", "History", "English", "Physics", "Chemistry",
                "Biology", "Computer Science", "Geography", "Physical Education", "Art", "Music", ]

    def subject(self):
        return self.random_element(self.subjects)


fake = Faker()
fake.add_provider(SubjectProvider)

TOKEN = os.environ.get('TOKEN')
api_url = "http://127.0.0.1:8000/api/students/"
authorization = f"Bearer {TOKEN}"

num_fake_names = 200

for _ in range(num_fake_names):
    first_name = fake.first_name()
    last_name = fake.last_name()
    payload = {
        "user": {"email": fake.email(),
                 "first_name": first_name,
                 "last_name": last_name,
                 "password": "password",
                 "confirm_password": "password",
                 },
        "course": fake.subject()
    }

    headers = {"Authorization": authorization,
               "Content-Type": "application/json"}

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Inserted: {first_name} {last_name}")
    else:
        print(f"Failed to insert: {first_name} {last_name}")
print("Done populating the database with fake names.")
