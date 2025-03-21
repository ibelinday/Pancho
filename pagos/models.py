from django.db import models

class Organizacion(models.Model):
     nombre = models.CharField(max_length=50)
     cuit = models.CharField(max_length=11, primary_key=True)

     def __str__(self):
          return f"{self.nombre} - {self.cuit}"

class Boleta(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.RESTRICT)
    codigo = models.AutoField(primary_key=True)
    fechaVencimiento = models.DateField("fecha de vencimiento")

    MESES = [
        (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'),
        (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'),
        (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'),
        (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
    ]
    
    periodo = models.IntegerField(choices=MESES)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    pagado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.codigo} - {self.get_periodo_display()} - ${self.monto}"