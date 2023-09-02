from django.db import models
# Create your models here.

class Book(models.Model):
    author = models.CharField(max_length=100)
    book = models.CharField(max_length=100, null=True)

class Quotes(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    quote = models.TextField()

class Question(models.Model):
    question = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)