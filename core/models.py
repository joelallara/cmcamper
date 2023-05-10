from django.db import models

class Listado(models.Model):
    descripcion = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ["-descripcion"]

    def __str__(self):
        return self.descripcion


class ListadoEquipamiento(Listado):

    class Meta:
        verbose_name = "Listado Equipamiento"
        verbose_name_plural = "Equipamientos"


class ListadoAccesorios(Listado):

    class Meta:
        verbose_name = "Listado Accesorio"
        verbose_name_plural = "Accesorios"


class SobreNosotros(models.Model):
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Sobre Nosotros"
        verbose_name_plural = "Sobre Nosotros"

    def __str__(self):
        return self.descripcion
    

class Contacto(models.Model):
    direccion = models.CharField(max_length=100, blank=True, null=True, default=None)
    localidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    numero_wspp = models.PositiveBigIntegerField(blank=True, null=True, default=None)
    mensaje_wspp = models.TextField(blank=True, null=True,default=None)
    link_facebook = models.URLField(max_length = 200, blank=True, null=True, default=None)
    link_instagram = models.URLField(max_length = 200, blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contacto"
        ordering = ["-localidad"]

    def __str__(self):
        return self.localidad


class Galeria(models.Model):
    imagen = models.ImageField(verbose_name="Imagen", upload_to="core")
    orden = models.PositiveIntegerField(unique=True)

    class Meta:
        abstract = True
        ordering = ["orden"]

    def __str__(self):
        return '{}'.format(self.orden)


class GaleriaProductos(Galeria):
    class Meta:
        verbose_name = "Galeria Productos"
        verbose_name_plural = "Galeria Productos"
        ordering = ["orden"]


class GaleriaMotorHome(Galeria):
    class Meta:
        verbose_name = "Galeria MotorHome"
        verbose_name_plural = "Galeria MotorHome"
        ordering = ["orden"]


class GaleriaPopup(Galeria):
    class Meta:
        verbose_name = "Galeria Popup"
        verbose_name_plural = "Galeria Popup"
        ordering = ["orden"]


class GaleriaOffRoad(Galeria):
    class Meta:
        verbose_name = "Galeria Camiones"
        verbose_name_plural = "Galeria Camiones"
        ordering = ["orden"]