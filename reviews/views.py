from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

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
    return render(request, 'publisher-detail.html', {
        'name': pub.name,
        'website': pub.website,
        'email': pub.email,
    })


# FBV <-->  CBV
def get_all_publisher(request):
    result = Publisher.objects.all().values()
    return render(request, 'publisher-list.html', {'publisher_list': result})


class TestView(View):
    def get(self, request):
        return HttpResponse('Hello from CBV')
