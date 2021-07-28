from django.urls import path

from book.views import list_book

app_name = "book"

urlpatterns = [
    path("list", list_book, name="list"),
]