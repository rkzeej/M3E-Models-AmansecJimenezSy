# Louis Amansec, 230286; Zeus Jimenez, 242359; Nathan Riley Sy, 244311
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

from django.contrib import admin

# Register your models here.
from .models import Supplier, WaterBottle

admin.site.register(Supplier)
admin.site.register(WaterBottle)