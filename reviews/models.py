from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return f'출판사명: {self.name}, 이메일: {self.email}'


class Book(models.Model):
    title = models.CharField(max_length=70)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')

    def __str__(self):
        return f'제목: {self.title}, isbn: {self.isbn}'


class Contributor(models.Model):
    first_names = models.CharField(max_length=50)
    last_names = models.CharField(max_length=50)
    email = models.EmailField()


class BookContributor(models.Model):
    class ContributorRole(models.TextChoices):
        AUTHOR = 'AUTHOR', 'Author'
        CO_AUTHOR = 'CO_AUTHOR', 'Co-Author'
        EDITOR = 'EDITOR', 'Editor'

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(choices=ContributorRole.choices, max_length=20)


class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(null=True)
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

