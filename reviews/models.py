from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()
    email = models.EmailField()
