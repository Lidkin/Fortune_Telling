from django.db import models
# Create your models here.

class Book(models.Model):
    author = models.CharField(max_length=100)
    book = models.CharField(max_length=100)

class Quotes(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    quote = models.TextField()