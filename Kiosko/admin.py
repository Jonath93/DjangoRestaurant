from django.contrib import admin

from .models import SaleOrder,MrpProduction,ProductTemplate
# Register your models here.
admin.site.register(SaleOrder)
admin.site.register(MrpProduction)
admin.site.register(ProductTemplate)