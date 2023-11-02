from django.shortcuts import render

from readlits.books.models import Book


def booksList(request):
    context = {}
    books = Book.objects.all()
    context["books"] = books
    return render(request, "books/books.html", context)
