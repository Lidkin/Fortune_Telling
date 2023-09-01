import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fortune.settings')
import django
django.setup()


from telling_app.models import *
from faker import Faker

fake = Faker()

def create_books(number):
    for _ in range(number):
        book = Book(
            author=fake.name(),
            book=fake.city()
        )
        book.save()

        quote = Quotes(
            quote=fake.text()
        )
        quote.save()

    print(f"CREATED {number} Books")


def fill_quotes(number):
    for _ in range(number):
        quote = Quotes(
            book_id=random.randrange(1,10),
            quote=fake.text()
            )
        quote.save()

# create_books(10)
fill_quotes(50)