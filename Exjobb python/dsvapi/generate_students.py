import os
import django
import random
from faker import Faker

# Initiera Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dsvapi.settings')
django.setup()

from students.models import Student

fake = Faker()

programs = ['DSV-kandidat', 'Datavetenskap', 'Datorspelsutveckling', 'Data Science', 'IT-management']

# Antal teststudenter du vill skapa
NUM_STUDENTS = 10000  # ← Ändra till t.ex. 10000 om du vill ha mycket

for _ in range(NUM_STUDENTS):
    Student.objects.create(
        name=fake.name(),
        email=fake.email(),
        program=random.choice(programs)
    )

print(f"{NUM_STUDENTS} studenter har skapats.")
