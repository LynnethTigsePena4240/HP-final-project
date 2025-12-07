from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
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

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            form.save()
            return redirect('homepage')
    else:
        form = BookForm()

    return render(request, 'books/add_edit_book.html', {'form': form, 'new_book': True})


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book,id=book_id)

    #check if the logged in user is the owner
    if book.user and book.user != request.user:
        raise PermissionDenied("you are not allowed to edit this book")

    form = BookForm(request.POST or None, instance = book)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    
    return render(request,'books/add_edit_book.html', {'form':form, 'new_book':False})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book,id=book_id)

    if book.user and book.user != request.user:
        raise PermissionDenied("you are not allowed to edit this book")

    if request.method == 'POST': 
        book.delete()
        return redirect('homepage')

    return render(request,'books/delete_confirm.html', {'book':book})

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer