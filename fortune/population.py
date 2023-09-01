import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fortune.settings')
import django
django.setup()


from rent.models import *
from faker import Faker

fake = Faker()

def create_books(number):
    for _ in range(number):
        book = Books(
            author=fake.city(),
            book=fake.book(),
            postal_code=fake.zipcode()
        )
        b.save()

        quote = Quotes(
            quote=fake.street_address()
        )
        quote.save()

    print(f"CREATED {number} Books")

