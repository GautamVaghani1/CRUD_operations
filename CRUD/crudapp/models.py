from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.id)

# Create your models here.
