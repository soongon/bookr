from django.http import HttpResponse
from django.shortcuts import render

from reviews.models import Publisher


def index(request):
    return HttpResponse('<h1>Hello World, 안녕하세요</h1>')


def hello(request):
    name = request.GET.get('name') or 'world'
    return HttpResponse(f'안녕하세요 {name}')


def hello_eng(request):
    return HttpResponse('Helllo ')


def hello_chn(request):
    return HttpResponse('ni hao')


def hello_template(request):
    return render(request, 'hello.html')


def get_publisher_by_id(request, id):
    pub = Publisher.objects.get(id=id)
    name = pub.name
    return render(request, 'publisher-detail.html', {
        'name': name,
    })
