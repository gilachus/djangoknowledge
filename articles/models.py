from django.db import models


class Article(models.Model):
    tittle = models.CharField(max_length=140)
    content = models.TextField()
