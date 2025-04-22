from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Line(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define primary key
    line_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.line_name

class Product(models.Model):
    id = models.AutoField(primary_key=True) # Explicitly define primary key
    product_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.product_name
    
class LineProduct(models.Model):
    id = models.AutoField(primary_key=True) # Explicitly define primary key
    line_id = models.ForeignKey(Line, on_delete=models.CASCADE, related_name='line_products')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='line_products')

    class Meta:
        unique_together = ('line_id', 'product_id')

    def __str__(self):
        return f"{self.line_id} - {self.product_id}"

class Shift(models.Model):
    id = models.AutoField(primary_key=True) # Explicitly define primary key
    shift_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.shift_name

class ProductionData(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    line = models.ForeignKey(Line, on_delete=models.CASCADE, related_name='production_data')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='production_data')
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='production_data')
    date = models.DateField(default=timezone.now)
    line_speed = models.FloatField()
    total_production = models.IntegerField()
    total_energy_consumed = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        # Add a unique constraint to prevent duplicate entries for the same line, product, shift, and date
        unique_together = ('line', 'product', 'shift', 'date')

    def __str__(self):
        return f"Production Data for {self.line} - {self.product} - {self.shift} on {self.date}"

