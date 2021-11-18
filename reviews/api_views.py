from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from reviews.models import Book
from reviews.serializers import BookSerializer


@api_view()
def hello_api(request):
    books = Book.objects.all()
    books_serialize = BookSerializer(books, many=True)
    return Response(books_serialize.data)

