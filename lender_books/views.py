from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import PermissionDenied
from .models import Book
# Create your views here.

def book_list_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    
    books = Book.objects.filter(user__id=request.user.id)

    # books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book_list.html', context=context)

def book_detail_view(request, pk=None):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    book = get_object_or_404(Book, id=pk)
    context = {
        'book': book,
    }

    return render(request, 'book_detail.html', context=context)