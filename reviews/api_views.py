from django.http import HttpResponse
from reviews.models import Book


def hello_api(request):
    books = Book.objects.all().values()
    return HttpResponse(books, content_type='application/json')

