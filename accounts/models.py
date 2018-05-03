from django.db import models

# Create your models here.

# Seuraavassa luodaan tapahtumalle malli, johon käyttäjä voi itse syöttää t
# tapahtuman nimen, kuvauksen sekä päivämäärän

class Tapahtuma(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=30)

    def __str__(self):
        return self.name
