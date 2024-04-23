from django.db import models
from ..dep.models import dep
# Create your models here.
class skills(models.Model):
    skill = models.CharField('Habilidad', max_length=50)
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'skill'
        verbose_name_plural = 'skills'
        ordering=['skill']
    def __str__(self):
        return self.skill # TODO
class employee(models.Model):
    #aqui se crea los campos del modelo y dentro del los campos se especidica los datos
    firstName=models.CharField("Nombre(s)", max_length=60)
    lastName = models.CharField('Apellido(s)', max_length=60)
    fullName = models.CharField("Nombre Completo",max_length=120,blank=True)
    email = models.EmailField('Email', max_length=50,unique=True)
    # contador
    # administrador
    # economista
    # ingeniero 
    # otro
    JOB_CHOICES=(
        ('0','Ingeniero'),
        ('1','Practicante'),
        ('2','Administrador'),
        ('3','Contador'),
        ('4','RH'),
        ('5','Cliente')
    )
    job = models.CharField('Puesto', max_length=1,choices=JOB_CHOICES)
    dep = models.ForeignKey(dep, on_delete=models.CASCADE)
    skill = models.ManyToManyField(skills)
    photo = models.ImageField('Foto', upload_to='empPhoto', height_field=None, width_field=None, max_length=None,blank=True,null=True)
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
        ordering=['id','firstName','lastName','email','dep']
        unique_together=('email',)
        
    def __str__(self):
        return str(self.firstName)+ ' ' +self.lastName+ ' ' +self.email+' '+self.job 
