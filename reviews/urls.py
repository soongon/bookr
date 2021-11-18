from django.urls import path

import reviews.views

urlpatterns = [
    path('', reviews.views.index),
    path('hello/', reviews.views.hello),
    path('hello/eng', reviews.views.hello_eng),
    path('hello/chn', reviews.views.hello_chn),
    path('hello/tmp', reviews.views.hello_template),
    path('publisher/<int:id>', reviews.views.get_publisher_by_id),
    path('publisher/', reviews.views.get_all_publisher),
    path('cbv/', reviews.views.TestView.as_view()),
]
