from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from .serializers import *
from .models import *

# Create your views here.

import random


class GetRandomquote(APIView):
    def get(self, request, book: str):
        try:
            book = Book.objects.get(book=book)
            book_serializer = BookSerializer(book)
            book_id = book_serializer.data["id"]
            quotes = Quotes.objects.all().filter(bood_id=book_id)
            quotes_serializer = QuotesSerializer(quotes, many=True)
            quotes_list = [quote["quote"] for quote in quotes_serializer.data]
            quote = quotes_list[random.randrange(0, len(quotes_list))]
            return Response(quote, status=HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=HTTP_404_NOT_FOUND)


class GetBooks(APIView):
    def get(self, request, pk=None, format=None):
        try:
            if pk is None:
                books = Book.objects.all()
                serializer = BookSerializer(books, many=True)
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                books = Book.objects.get(id=pk)
                serializer = BookSerializer(books)
                return Response(serializer.data)
        except Exception as e:
            return Response({"message": str(e)}, status=HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, pk: int, *args, **kwargs):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk: int, *args, **kwargs):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response({"Message": f"Deleted book: {book.book}"})