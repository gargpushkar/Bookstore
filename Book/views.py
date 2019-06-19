from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Book


class BookListView(ListView):
    """Show all books."""

    model = Book


class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = 'isbn'

    # def get_queryset(self):
    #     isbn = get_object_or_404(Book, isbn=self.kwargs.get('isbn'))
    #     return Book.objects.filter(isbn=isbn)


class BookCreateView(CreateView):
    pass


class BookUpdateView(UpdateView):
    model = Book


class BookDeleteView(DeleteView):
    model = Book
