from django.db import models
from ..dep.models import Dep
# Create your models here.
class Empleado(models.Model):
    firstName=models.CharField("Nombre(s)", max_length=60)
    lastName = models.CharField('Apellido(s)', max_length=60)
    email = models.EmailField('Email', max_length=50,unique=True)
    # contador
    # administrador
    # economista
    # ingeniero 
    # otro
    JOB_CHOICES=(
        ('0','contador'),
        ('1','administrador'),
        ('2','economista'),
        ('3','ingeniero'),
        ('4','otro')
    )
    job = models.CharField('Puesto', max_length=1,choices=JOB_CHOICES)
    dep = models.ForeignKey(Dep, on_delete=models.CASCADE)
    #FOTO = models.ImageField('Foto', upload_to=None, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return str(self.firstName)+ ' ' +self.lastName+ ' ' +self.email+' '+self.job 