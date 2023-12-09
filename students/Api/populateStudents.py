import requests
from faker import Faker
from faker.providers import BaseProvider


class SubjectProvider(BaseProvider):
    subjects = ["Mathematics", "Science", "History", "English", "Physics", "Chemistry",
                "Biology", "Computer Science", "Geography", "Physical Education", "Art", "Music", ]

    def subject(self):
        return self.random_element(self.subjects)


fake = Faker()
fake.add_provider(SubjectProvider)

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyMTE1MjY5LCJpYXQiOjE3MDIxMDgwNjksImp0aSI6IjM5ZjkyYjQzMTc2NjQ3ZTE4YjBhZjQxNTlkOTkwODc1IiwidXNlcl9pZCI6IjAyNTg5YTZiLWVkZGEtNDMwNi1hOWZiLTNiMDZmMDY4YzZjNSJ9.FuSDFpmwBzLR53DnYgnY2bnTgsdaUnj10hA07nm8tOA"
api_url = "http://127.0.0.1:8000/api/students/"
authorization = f"Bearer {TOKEN}"

num_fake_names = 100

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
