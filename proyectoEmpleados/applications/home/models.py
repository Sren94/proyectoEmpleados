from django.db import models

# Create your models here
#creando una tabla con ORM
class prueba(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    