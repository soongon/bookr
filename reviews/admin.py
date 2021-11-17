from django.contrib import admin

from reviews.models import Book, Publisher, Contributor, Review, BookContributor

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Review)
admin.site.register(BookContributor)
