from django.db import models


class Quote(models.Model):

    custom_name = models.CharField(max_length=120)
    quotes = models.TextField(max_length=254)
