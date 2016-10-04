from django.contrib import admin

from .models import SaleOrder,MrpProduction
# Register your models here.
admin.site.register(SaleOrder)
admin.site.register(MrpProduction)