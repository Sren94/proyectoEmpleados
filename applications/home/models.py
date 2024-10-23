from django.db import models

# Create your models here
#creando una tabla con ORM
class prueba(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.BigIntegerField()
    
    def __str__(self):
        return self.titulo+' '+self.subtitulo+' '+str(self.cantidad)