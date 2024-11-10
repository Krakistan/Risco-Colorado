from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    
    TIPO_CHOICES = [
        ('Venta', 'Venta'),
        ('Arriendo', 'Arriendo'),
    ]
    
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        default='Venta'
    )
    
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Cotizacion(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    
