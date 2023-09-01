from rest_framework import serializers
from .models import Book, Quotes, Question


class BookSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Book
        fields = "__all__"
        

class QuotesSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Quotes
        fields = "__all__"
        
        
class QuestionSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Question
        fields = "__all__"