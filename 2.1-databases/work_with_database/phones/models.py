from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    release_date = models.DateField(max_length=100)
    lte_exists = models.BooleanField(max_length=100)
    slug = models.SlugField(max_length=100)