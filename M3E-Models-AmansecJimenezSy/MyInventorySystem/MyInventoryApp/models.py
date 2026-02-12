from django.db import models

# Create your models here.

class Supplier(models.Model): 
    name = models.CharField(max_length=100) 
    city = models.CharField(max_length=100) 
    country = models.CharField(max_length=100) 
    createdat = models.DateTimeField() 
    
    def getName(self): 
        return self.name 
    
    def __str__(self): 
        return f"{self.name} - {self.city}, {self.country} created at: {self.createdat}"

class WaterBottle(models.Model): 
    sku = models.CharField(max_length=10, unique=True) 
    brand = models.CharField(max_length=100) 
    cost = models.DecimalField(max_digits=10, decimal_places=2) 
    size = models.CharField(max_length=50) 
    mouthsize = models.CharField(max_length=50) 
    color = models.CharField(max_length=50) 
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE) 
    currentquant = models.IntegerField() 
    
    def __str__(self): 
        return (f"{self.sku}: {self.brand}, {self.mouthsize}, {self.size}, {self.color}, " f"supplied by {self.supplier.name}, Cost: {self.cost} : {self.currentquant}")