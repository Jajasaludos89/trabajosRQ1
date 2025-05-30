from django.db import models # type: ignore

# Create your models here.
class Cargo(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    funciones=models.TextField()
    horario=models.CharField(max_length=500)
    requisitos=models.TextField()
    sueldo=models.DecimalField(max_digits=10,decimal_places=2)

    
    logo=models.FileField(upload_to='cargo', null=True, blank=True)

    #para visualizar los datos de mejor manera
    def __str__(self):
        fila="{0}: {1} {2} {3}"
        return fila.format(self.id,self.nombre,self.sueldo,self.horario)


    



