from django.db import models


class Item(models.Model):
    url = models.TextField()
    interval = models.PositiveSmallIntegerField()
    
    objects = models.Manager()


class History(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    response = models.TextField(null=True)
    duration = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    
    objects = models.Manager()
