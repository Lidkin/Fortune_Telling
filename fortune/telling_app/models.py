from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=100)
    book = models.CharField(max_length=100, null=True)


class Quotes(models.Model):
    quote = models.TextField(max_length=300)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)


class Questions(models.Model):
    pattern = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    