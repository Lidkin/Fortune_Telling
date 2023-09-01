from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=100)
    book = models.CharField(max_length=100, null=True)


class Quotes(models.Model):
    bood_id = models.ForeignKey("Book", on_delete=models.CASCADE, null=True)
    quote = models.TextField(max_length=300)


class Question(models.Model):
    question = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
