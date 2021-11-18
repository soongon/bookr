from django.contrib import admin
from django.urls import path, include

import reviews.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(reviews.urls)),
]
