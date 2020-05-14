from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    costo = MoneyField(max_digits=14, decimal_places=0, default_currency='MXN')

    def __str__(self):
        return self.nombre


class ExchangeRate(models.Model):
    base_currency = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=20, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s a %s' % (self.base_currency, self.currency)
