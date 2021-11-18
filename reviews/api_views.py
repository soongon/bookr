from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from reviews.models import Book
from reviews.serializers import BookSerializer

from rest_framework import generics
from rest_framework import viewsets


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer




# @api_view()
# def hello_api(request):
#     books = Book.objects.all()
#     books_serialize = BookSerializer(books, many=True)
#     return Response(books_serialize.data)

# class HelloApi(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
