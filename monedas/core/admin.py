from django.contrib import admin
from .models import Servicio, ExchangeRate


# Register your models here.
@admin.register(Servicio)
class AdminServicio(admin.ModelAdmin):
    pass

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    pass
