from faker import Faker
from pprint import pprint

fake = Faker()


fake_parents = []
for _ in range(50):
    father_name = fake.name()
    father_phone = fake.phone_number()
    mother_name = fake.name()
    mother_phone = fake.phone_number()
    fake_parents.append({
        'father': {'name': father_name, 'phone': father_phone},
        'mother': {'name': mother_name, 'phone': mother_phone}
    })

pprint(fake_parents)