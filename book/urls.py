from django.urls import path

from book.views import BookView, list_book

app_name = "book"

urlpatterns = [
    path("<int:book_id>", BookView.as_view(), name="get"),
    path("list", list_book, name="list"),
]