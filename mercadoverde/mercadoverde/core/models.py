from distutils.command.upload import upload
from email.mime import image
from operator import mod
from pyexpat import model
from statistics import mode
from tkinter import N
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    CategoryId = models.AutoField(primary_key = True, verbose_name = 'CATEGORIAID')
    name = models.CharField(max_length = 25, verbose_name = 'CATEGORIANOMBRE')

    def __str__(self):
        return self.name

class Product(models.Model):
    ProductId = models.AutoField(primary_key = True, verbose_name = 'PRODUCTOID')
    name = models.CharField(max_length = 50, verbose_name = 'PRODUCTONOMBRE')
    price = models.FloatField(verbose_name = 'PRODUCTOPRECIO')
    description = models.TextField(max_length = 200, verbose_name = 'PRODUCTODESCRIPCION')
    image = models.ImageField(null =  True, blank = True, verbose_name = 'PRODUCTOIMAGEN', upload_to = 'medias')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
