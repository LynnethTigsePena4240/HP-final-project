from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('book_detail/<int:book_id>/', views.book_detail, name = 'book_detail'),

    path('add/', views.add_book, name = 'add_book'),
    path('edit/<int:book_id>/', views.edit_book, name = 'edit_book'),
    path('delete/<int:book_id>', views.delete_book, name = 'delete_book'),
    path('api/books/', views.BookList.as_view(),name='book-list-create'),
    path('api/books/<int:pk>/', views.BookDetailView.as_view(),name='book-detail')
]