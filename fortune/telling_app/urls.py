from django.urls import path
from .views import *

urlpatterns = [
    path('books/', GetBooks.as_view(), name='books'),
    path('book/<str:book>', GetRandomquote.as_view(), name='book'),
    path('question', UserQuestion.as_view(), name='question'),
]