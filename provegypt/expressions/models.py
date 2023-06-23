from django.db import models


class Expression(models.Model):
    version_ar = models.CharField(max_length=1000)
    version_fra = models.CharField(max_length=1000)
    populaire = models.BooleanField(default=False)
    explication = models.CharField(max_length=1000)
    nom = models.CharField(max_length=100, default='test')

    def __str__(self):
        return self.nom



# Create your models here.
