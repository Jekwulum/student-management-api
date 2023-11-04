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

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1Mjk1MzAzLCJpYXQiOjE2OTUyOTIzMDMsImp0aSI6IjMzMmMzN2MyYjFkZTQwYjk5YTdjMGY4OWNjYjBiMTNhIiwidXNlcl9pZCI6IjdiNDAzNDZiLThhM2QtNGQ0Yi05ZjdmLThhYmUwMTM3MmQxMSJ9._EZ8qHkD0ZvTx4GM7eWosuM3Ezex7bkVMpCH_zckixQ"
api_url = "http://127.0.0.1:8000/api/students/"
authorization = f"Bearer {TOKEN}"

num_fake_names = 150

for _ in range(num_fake_names):
    first_name = fake.first_name()
    last_name = fake.last_name()
    payload = {
        "user": {"email": fake.email(),
                 "first_name": first_name,
                 "last_name": last_name,
                 "password": "password",
                 "confirm_password": "password"
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
