from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK,
                                     HTTP_400_BAD_REQUEST,
                                     HTTP_404_NOT_FOUND)

from .serializers import *
from .models import *

# Create your views here.

import random

class GetRandomquote(APIView):

    def get(self, request, book:str):
        try:
            book = Book.objects.get(book=book)
            book_serializer = BookSerializer(book)
            book_id = book_serializer.data['id']
            quotes = Quotes.objects.all().filter(book_id=book_id)
            quotes_serializer = QuotesSerializer(quotes, many=True)
            quotes_list = [quote['quote'] for quote in quotes_serializer.data]
            quote = quotes_list[random.randrange(0, len(quotes_list))]
            return Response(quote, status=HTTP_200_OK)
        except Exception as e:    
            return Response({"message":str(e)}, status=HTTP_404_NOT_FOUND)    

class GetBooks(APIView):
    def get(self, request):
        try:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:    
            return Response({"message":str(e)}, status=HTTP_404_NOT_FOUND)      

class UserQuestion(APIView):
    def post(self, request):
        serializer = QuestionsSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            try:
                question = Questions.objects.get(question=serializer['question'])
                question.count += 1
                question.save()
            except Questions.DoesNotExist:
                new_question = Questions(pattern=serializer['pattern'], question=serializer['question'], count=1)
                new_question.save()
            return Response(serializer.data)
        return Response(serializer.errors)    

    def get(self, request):
        try:
            questions = Questions.objects.all()
            serializer = QuestionsSerializer(questions, many=True)   
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:    
            return Response({"message":str(e)}, status=HTTP_404_NOT_FOUND)           
