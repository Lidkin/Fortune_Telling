import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fortune.settings")
import django

django.setup()

from telling_app.models import Book, Quotes
from quote import quote


def create_book_list(quotes_data):
    
    for el in quotes_data:
        author = el["author"]
        book_title = el["book"]
        book = Book(author=author, book=book_title)
        book.save()

        quote = Quotes(bood_id=book, quote=el["quote"])
        quote.save()
        
    print("CREATED")

create_book_list(quote("harry potter", limit=10))
