from django.db import models
from datetime import datetime

# Create your models here.

class Empleado(models.Model):
    nombres = models.CharField(max_length=150,verbose_name='Nombres')
    dni = models.CharField(max_length=8,unique=True,verbose_name='Dni')
    date_joined = models.DateField(default=datetime.now,verbose_name='Fecha_Registro')

    #auto_now_add :reeplaza la fecha con la ultima con la que se inserto 
    #auto_now: la primera vez que se inserta guarda la fecha y nada mas
    date_updated = models.DateTimeField(auto_now_add=True)
    
    #existe integerfield = int / positive intergerField = 0 >= x
    age = models.PositiveIntegerField(default=0)
    
    salario = models.DecimalField(default=0.0,max_digits=6,decimal_places=2)
    estado = models.BooleanField(default=True)
    
    # upload to = archivos en carpetas especifica- se puede configurar que guarde como año mes y dia (/%Y/%m/%d)
    perfil = models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    #existe fileField para archivos (req instalar la libreria Pillow) para imagenes

    #valores de retorno por defecto de la clase
    def __str__(self):
        return self.nombres
    
    #propiedades de la entidad (opcional)
    class Meta:
        #nombre de la tabla
        db_table ='empleado'
        #el nombre cuando se registre en el modulo de administracion de django
        verbose_name = 'Empleado'
        verbose_name_plural ='Empleados'
        #como se ordena en un listado
        ordering = ['id']

