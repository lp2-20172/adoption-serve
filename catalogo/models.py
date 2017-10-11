from django.db import models
from core.models import User, Person

# Create your models here.


class Categoria(models.Model):

    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return '%s' % (self.nombre)



class Mascota(models.Model):

    nombre = models.CharField(max_length=60)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.CharField(max_length=60)
    fecha_rescate = models.DateField(null=True)

    categoria = models.ManyToManyField(
    "Categoria",
    verbose_name="list of Categorias",
    null=True,  blank=True)


    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return '%s' % (self.nombre)


class Cliente(models.Model):

    nombre = models.CharField(max_length=60)
    edad = models.CharField(max_length=10)
    telefono = models.CharField(max_length=60)
    email = models.DateField(null=True)
    domicilio = models.DateField(null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s' % (self.nombre)





