from django.contrib import admin

from .models import SaleOrder,MrpProduction,ProductTemplate,PosCategory
# Register your models here.
admin.site.register(SaleOrder)
admin.site.register(PosCategory)
admin.site.register(MrpProduction)
admin.site.register(ProductTemplate)