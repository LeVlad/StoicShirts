from django.db import models
from products.models import Philosopher


class StoicQuotes(models.Model):
    stoic = Philosopher()
    most_popular = models.IntegerField()
