from django.db import models


class InspirationalQuote(models.Model):
    custom_name = models.CharField(max_length=15, null=True)
    quote = models.TextField(max_length=254, null=True)


IDEAS= (
    ('w', 'Wisdom'),
    ('c', 'Courage'),
    ('m', 'Mderation'),
    ('j', 'Justice'),
)
stoic_idea = models.CharField(max_length=255, choices=IDEAS, default='wisdom')
