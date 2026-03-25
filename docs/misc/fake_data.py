"""Generate fake person data (50 European persons) and save as CSV and JSON."""

import csv
import json
import random
from faker import Faker

# European locales for realistic addresses
locales = ["de_DE", "fr_FR", "it_IT", "es_ES", "nl_NL", "de_AT", "de_CH", "pt_PT"]
fake = Faker(locales)
Faker.seed(42)
random.seed(42)

hobby_pool = [
    "reading", "cycling", "hiking", "cooking", "photography", "gardening",
    "swimming", "chess", "painting", "yoga", "running", "music", "knitting",
    "traveling", "fishing", "dancing", "tennis", "skiing", "baking", "writing",
]

persons = []
for _ in range(50):
    n_hobbies = random.randint(1, 4)
    persons.append({
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "street": fake.street_address(),
        "town": fake.city(),
        "zip": fake.postcode(),
        "country": fake.current_country(),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
        "hobbies": random.sample(hobby_pool, n_hobbies),
    })

# Save as JSON
with open("misc/person.json", "w", encoding="utf-8") as f:
    json.dump(persons, f, indent=2, ensure_ascii=False)

# Save as CSV (hobbies as semicolon-separated string)
with open("misc/person.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "first_name", "last_name", "street", "town", "zip", "country",
        "date_of_birth", "hobbies",
    ])
    writer.writeheader()
    for p in persons:
        row = dict(p)
        row["hobbies"] = ";".join(row["hobbies"])
        writer.writerow(row)

print(f"Created misc/person.json and misc/person.csv with {len(persons)} persons.")
