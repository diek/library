from rest_framework import generics

from book.models import Book
from .seriallizers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    seriallizer_class = BookSerializer
