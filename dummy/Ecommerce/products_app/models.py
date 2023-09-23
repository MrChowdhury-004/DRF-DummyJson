from django.db import models

from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=400, default='')
    

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=255)
    thumbnail = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    rating = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=0)
    brands = models.ManyToManyField(Brand)  # Establish ManyToMany relationship with Brand

    def __str__(self):
        return self.title








# class Brand(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
#     def __str__(self):
#         return self.name
    


# class Product(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=400)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
#     rating = models.FloatField()
#     stock = models.PositiveIntegerField()
#     brands = models.ManyToManyField(Brand)  # Establish the relationship
#     category = models.CharField(max_length=255)
#     thumbnail = models.URLField()

#     def __str__(self):
#         return self.title

