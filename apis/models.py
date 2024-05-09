from django.db import models


class WordCount(models.Model):
    url = models.CharField(max_length=250, null=True, blank=True)
    word = models.CharField(max_length=100, null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
