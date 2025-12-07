from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import Book
from .forms import BookForm
from .serializers import BookSerializer

# Create your views here.
def homepage(request):
    books = Book.objects.all()
    return render(request,'books/homepage.html', {'books':books})

def book_detail(request,book_id):
    books = Book.objects.get(id=book_id)
    return render(request,'books/book_detail.html', { 'book':books})

# @login_required (uncomment later when add book is working)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm()

    return render(request, 'books/add_edit_book.html', {'form': form, 'new_book': True})


# @login_required (uncomment later when edit book is working)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(request.POST or None, instance = book)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    
    return render(request,'books/add_edit_book.html', {'form':form, 'new_book':False})

# @login_required (uncomment later when delete book is working)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST': 
        book.delete()
        return redirect('homepage')

    return render(request,'books/add_edit_book.html', {'book':book})

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer