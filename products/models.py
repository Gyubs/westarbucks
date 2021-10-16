from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name     = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    allegies = models.ManyToManyField('Allegy')

    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return self.name

class Allegy(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'allegies'

    def __str__(self):
        return self.name
        