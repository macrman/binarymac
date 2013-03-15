from django.db import models


class Container(models.Model):
    path = models.CharField(max_length=100)
