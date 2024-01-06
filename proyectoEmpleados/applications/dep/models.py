from django.db import models

# Create your models here.
class Dep(models.Model):
    name = models.CharField('Nombre', max_length=60,blank=True)
    shortName = models.CharField('Nombre Corto', max_length=20,unique=True)
    anulate = models.BooleanField('Anulado',default=False)
    def __str__(self):
        return str(self.id)+ ' ' +self.name+ ' ' +self.shortName
    