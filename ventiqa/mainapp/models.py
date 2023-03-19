from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True, default='')
    name = models.CharField(max_length=100)
    remaining_stock = models.IntegerField(default=-1)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Products'

class Subscription(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.product} ({self.duration} months)'
    
    class Meta:
        verbose_name_plural = 'Subscriptions'