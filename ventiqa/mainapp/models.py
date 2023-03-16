from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    available_quantity = models.IntegerField(verbose_name='Available quantity', null=True, blank=True, default=-1)
    price_1m = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price per month', null=True, blank=True)
    price_3m = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price per 3 months', null=True, blank=True)
    price_6m = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price per 6 months', null=True, blank=True)
    price_12m = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price per 12 months', null=True, blank=True)

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'