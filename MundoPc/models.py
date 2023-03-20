from django.db import models

class Procesador(models.Model):
    nombre = models.CharField(max_length=100)
    ghz = models.FloatField()
    nucleos = models.IntegerField()
    hilos = models.IntegerField()
    precio = models.IntegerField()
    posicion = models.IntegerField()

    def __str__(self):
        return self.nombre

class Gpu(models.Model):
    nombre = models.CharField(max_length=100)
    vram = models.IntegerField()
    pines = models.IntegerField()
    precio = models.IntegerField()
    posicion = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Disco(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=100)
    precio = models.FloatField()
    posicion = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Ram(models.Model):
    nombre = models.CharField(max_length=100)
    memoria = models.IntegerField()
    frecuencia = models.IntegerField()
    precio = models.FloatField()
    posicion = models.IntegerField()
    
    def __str__(self):
        return self.nombre 
