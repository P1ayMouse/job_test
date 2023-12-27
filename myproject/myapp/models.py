from django.db import models


class Person(models.Model):
    name = models.CharField(null=False, max_length=100)
    surname = models.CharField(null=False, max_length=100)
    age = models.IntegerField(null=False)
