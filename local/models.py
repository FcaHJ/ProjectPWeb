from django.db import models

# Create your models here.
class Rol(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Boleta(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name

class Detalle_Boleta(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField(max_length=200)
    price = models.IntegerField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    