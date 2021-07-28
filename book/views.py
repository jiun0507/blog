from django.shortcuts import render
from book.models import Book
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views import View
from django.http import Http404


def list_book(request):
    try:
        all_books = Book.objects.all().order_by("-created_at")
        page = int(request.GET.get("p", 1))  # 없으면 1로 지정
        paginator = Paginator(all_books, 5)  # 한 페이지 당 몇개 씩 보여줄 지 지정
        books = paginator.get_page(page)
    except Book.DoesNotExist:
        return redirect("404.html")

    context = {
        "books": books,
    }
    return render(request, "book/books.html", context=context)


class BookView(View):
    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            raise Http404
        context = {
            "book": book,
        }
        return render(request, "book/book.html", context=context)
