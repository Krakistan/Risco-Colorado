
from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    
    # Categorías posibles para productos
    CATEGORIA_CHOICES = [
        ('Materiales de Construcción', 'Materiales de Construcción'),
        ('Cemento y Hormigón', 'Cemento y Hormigón'),
        ('Arena y Áridos', 'Arena y Áridos'),
        ('Grava y Piedra', 'Grava y Piedra'),
        ('Maicillo', 'Maicillo'),
        ('Ladrillos y Bloques', 'Ladrillos y Bloques'),
        ('Yeso y Mortero', 'Yeso y Mortero'),
        ('Acero y Varillas', 'Acero y Varillas'),
        ('Madera y Tableros', 'Madera y Tableros'),
        ('Aislantes e Impermeabilizantes', 'Aislantes e Impermeabilizantes'),
        ('Maquinaria Pesada', 'Maquinaria Pesada'),
        ('Retroexcavadoras', 'Retroexcavadoras'),
        ('Excavadoras', 'Excavadoras'),
        ('Bulldozers', 'Bulldozers'),
        ('Motoniveladoras', 'Motoniveladoras'),
        ('Compactadoras y Rodillos', 'Compactadoras y Rodillos'),
        ('Cargadores Frontales', 'Cargadores Frontales'),
        ('Gruas y Montacargas', 'Gruas y Montacargas'),
        ('Dumpers y Camiones Tolva', 'Dumpers y Camiones Tolva'),
        ('Herramientas Eléctricas', 'Herramientas Eléctricas'),
        ('Taladros y Rotomartillos', 'Taladros y Rotomartillos'),
        ('Amoladoras y Pulidoras', 'Amoladoras y Pulidoras'),
        ('Sierras y Cortadoras', 'Sierras y Cortadoras'),
        ('Generadores Eléctricos', 'Generadores Eléctricos'),
        ('Compresores de Aire', 'Compresores de Aire'),
        ('Martillos Neumáticos', 'Martillos Neumáticos'),
        ('Equipos para Construcción', 'Equipos para Construcción'),
        ('Andamios y Escaleras', 'Andamios y Escaleras'),
        ('Mezcladoras de Cemento', 'Mezcladoras de Cemento'),
        ('Torres de Iluminación', 'Torres de Iluminación'),
        ('Vibradores de Concreto', 'Vibradores de Concreto'),
        ('Bateas y Carretillas', 'Bateas y Carretillas'),
        ('Equipos de Protección Personal', 'Equipos de Protección Personal'),
        ('Cascos de Seguridad', 'Cascos de Seguridad'),
        ('Guantes y Gafas de Protección', 'Guantes y Gafas de Protección'),
        ('Chalecos Reflectantes', 'Chalecos Reflectantes'),
        ('Botas de Seguridad', 'Botas de Seguridad'),
        ('Arnés y Equipos de Altura', 'Arnés y Equipos de Altura'),
        ('Accesorios y Repuestos', 'Accesorios y Repuestos'),
        ('Repuestos para Maquinaria', 'Repuestos para Maquinaria'),
        ('Lubricantes y Aceites', 'Lubricantes y Aceites'),
        ('Filtros y Mangueras', 'Filtros y Mangueras'),
        ('Equipos para Transporte', 'Equipos para Transporte'),
        ('Carros de Mano', 'Carros de Mano'),
        ('Pallets y Elevadores', 'Pallets y Elevadores'),
        ('Cintas Transportadoras', 'Cintas Transportadoras'),
        ('Equipos para Demolición', 'Equipos para Demolición'),
        ('Martillos Hidráulicos', 'Martillos Hidráulicos'),
        ('Cortadoras de Pavimento', 'Cortadoras de Pavimento'),
        ('Perforadoras y Equipos de Demolición', 'Perforadoras y Equipos de Demolición')
    ]
    
    categoria = models.CharField(
        max_length=255,
        choices=CATEGORIA_CHOICES,
        default='Construcción'
    )
    
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

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    nombre_cliente = models.CharField(max_length=50)
    fecha = models.DateField()

class ProductosCompra(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    cantidad = models.IntegerField()


class Cotizacion(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    