
from django.db import models

# Create your models here.

# breed class
class Breed(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# cat class
class Cat(models.Model):
    nickname = models.CharField(max_length=200)
    weight = models.FloatField()
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE, null=False)
    foods = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nickname