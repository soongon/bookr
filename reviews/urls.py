from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views, api_views

router = DefaultRouter()
router.register('books', api_views.BookViewSet)
# todo router.register('books', api_views.BookViewSet)

urlpatterns = [
    # path('api/hello/', api_views.hello_api),
    path('api/', include(router.urls)),

    path('', views.index),
    path('hello/', views.hello),
    path('hello/eng', views.hello_eng),
    path('hello/chn', views.hello_chn),
    path('hello/tmp', views.hello_template),
    path('publisher/<int:id>', views.get_publisher_by_id),
    path('publisher/', views.get_all_publisher),
    path('cbv/', views.TestView.as_view()),
]
