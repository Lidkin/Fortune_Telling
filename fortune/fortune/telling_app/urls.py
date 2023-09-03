from django.urls import path, include
from telling_app.views import GetBooks, GetRandomquote, QuotesBooks, UserQuestion, dashboard_view

urlpatterns = [
    path("books/", GetBooks.as_view(), name="books"),
    path("books/get_book/<int:pk>/", GetBooks.as_view(), name="books"),
    path("book/<str:book>", GetRandomquote.as_view(), name="book"),
    path("quotes/", QuotesBooks.as_view(), name="quotes"),
    path('questions/', UserQuestion.as_view(), name='question'),
    path('form/', dashboard_view, name='form')
]
