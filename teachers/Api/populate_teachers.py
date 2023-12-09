import requests
import os
from dotenv import load_dotenv
from faker import Faker
from faker.providers import BaseProvider
from pprint import pprint
import random

load_dotenv()
fake = Faker()

TOKEN = os.environ.get('TOKEN')
api_url = "http://127.0.0.1:8000/api/teachers/"
authorization = f"Bearer {TOKEN}"

num_fake_data = 5

existing_teachers = ['d58791f1-c8fd-4562-83db-74508406a243', 'c11833fa-a466-4d29-8f7e-903451a40b5e', '33bf7117-a98d-4794-b600-888a6feee39b', 'dd082dda-4874-4370-85a8-11c95e34b8c2', '1fabf320-4562-4293-b8a1-6a5146a54f50', '80eb1f4d-775d-439b-9ce6-16f350c13a22', 'a0cc5137-f733-444e-a05b-534b23b91449', 'f26a73d6-676d-41b2-9a04-93ad361e05c0', '91b35fec-dbb4-4597-b1ef-cf10813a0260', 'f69d0adf-218f-45ae-ad82-86e581a70bbb',
                     'e79306ba-22d6-42d3-9fa2-f7b967b3ff7c', '7c919c85-b427-466f-9ea2-3a50194d69ea', 'd04ed63a-09d4-4878-8aff-c7217be92885', 'cb8d1545-8b8c-497b-93e1-dbfacb8a80c7', '7eca6762-7991-4771-ad21-6022c275b906', 'dc786a77-563f-4efb-a584-a92a6e0f4c86', 'a6c1caf6-a0f3-471f-8cde-68d1072df0da', 'ded7a962-4f14-4d0b-9a7c-972ddd0eb8c7', '9be2e961-28ce-43e7-9818-eb68ca70ea98', '814baa33-bba6-4ab2-8248-b551a03681ff']

for idx in range(len(existing_teachers)):
    user = existing_teachers[idx]
    payload = {"user": user}

    headers = {"Authorization": authorization,
               "Content-Type": "application/json"}

    response = requests.post(api_url, json=payload, headers=headers)

    pprint(response.json())

    if response.status_code == 201 or response.status_code == 200:
        print(f"Inserted: {user}")
        # user_ids.append(response.data.user_id)
    else:
        print(f"Failed to insert: {user}")
print("Done populating the database with fake names.")
