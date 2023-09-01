from rest_framework import serializers
from .models import *

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'

class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'        