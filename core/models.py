from django.db import models
from datetime import datetime

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Type')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        db_table = "tipo"
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Categoria')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "categoria"
        ordering = ['id']


class Employed(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    names = models.CharField(max_length=150, verbose_name='Nombre')
    ci = models.CharField(max_length=11, verbose_name='Carnet de Identidad', unique=True)
    date_joined = models.DateTimeField(default=datetime.now, verbose_name="Fecha de Registro")
    date_creation = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00,max_digits=9,decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    cvitae = models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)


    def __str__(self):
        return self.names

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = "empleado"
        ordering = ['id']
