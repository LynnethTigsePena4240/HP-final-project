from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
def homepage(request):

    return render(request,'books/homepage.html')

def book_detail(request):

    return render(request,'books/book_detail.html')

# @login_required (uncomment later when add book is working)
def add_book(request):

    return render(request,'books/add_edit_book.html')

# @login_required (uncomment later when edit book is working)
def edit_book(request):

    return render(request,'books/add_edit_book.html')

# @login_required (uncomment later when delete book is working)
def delete_book(request):

    return render(request,'books/add_edit_book.html')

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer