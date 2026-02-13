# Louis Amansec, ######; Zeus Jimenez, 242359; Nathan Riley Sy, 244311
# February 13, 2026 

'''
I hereby attest to the truth of the following facts:

I have not discussed the Python language code in my program with anyone
other than my instructor or the teaching assistants assigned to this course.

I have not used Python language code obtained from another student, or
any other unauthorized source, either modified or unmodified.

If any Python language code or documentation used in my program was
obtained from another source, such as a textbook or course notes, that has been clearly noted with proper citation in the
comments of my program.
'''

from django.db import models

# Create your models here.

class Supplier(models.Model): 
    name = models.CharField(max_length=100) 
    city = models.CharField(max_length=100) 
    country = models.CharField(max_length=100) 
    created_at = models.DateTimeField() 
    
    def getName(self): 
        return self.name 
    
    def __str__(self): 
        return f"{self.name} - {self.city}, {self.country} created_at: {self.created_at}"

class WaterBottle(models.Model): 
    SKU = models.CharField(max_length=10, unique=True) 
    brand = models.CharField(max_length=100) 
    cost = models.DecimalField(max_digits=10, decimal_places=2) 
    size = models.CharField(max_length=50) 
    Mouth_Size = models.CharField(max_length=50) 
    color = models.CharField(max_length=50) 
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE) 
    Current_Quantity = models.IntegerField() 
    
    def __str__(self): 
        return (f"{self.SKU}: {self.brand}, {self.Mouth_Size}, {self.size}, {self.color}, " f"supplied by {self.supplied_by.name}, Cost: {self.cost} : {self.Current_Quantity}")