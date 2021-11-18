from django.urls import path

from . import views, api_views

urlpatterns = [
    path('api/hello/', api_views.hello_api),

    path('', views.index),
    path('hello/', views.hello),
    path('hello/eng', views.hello_eng),
    path('hello/chn', views.hello_chn),
    path('hello/tmp', views.hello_template),
    path('publisher/<int:id>', views.get_publisher_by_id),
    path('publisher/', views.get_all_publisher),
    path('cbv/', views.TestView.as_view()),
]
