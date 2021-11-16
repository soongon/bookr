from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=70)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)


class Contributor(models.Model):
    first_names = models.CharField(max_length=50)
    last_names = models.CharField(max_length=50)
    email = models.EmailField()
