from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    nom = models.CharField(max_length=30)
    mail = models.EmailField(blank=True)
    message = models.TextField()