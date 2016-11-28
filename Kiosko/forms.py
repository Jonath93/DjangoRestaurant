from django import forms
from .models import SaleOrder,SaleOrderLine,SaleOrderTax
from datetime import datetime

ESTADO = (
    ('MAN','manual'),
    ('DRA','draft'),
    ('CAN','cancel')
)



class SaleOrderLineForm(forms.ModelForm):
    class Meta:
        model=SaleOrderLine

        fields=[
            'product_uos_qty',
            'price_unit',
            'product_uom_qty',
            'name',
            'product_id'
        ]

        widgets = {
            'product_uos_qty':forms.TextInput(attrs={'class': 'cantidadformulario','type':'hidden'}),
            'price_unit':forms.TextInput(attrs={'class': 'precioformulario','type':'hidden'}),
            'product_uom_qty':forms.TextInput(attrs={'class': 'cantidad2formulario','type':'hidden'}),
            'name':forms.TextInput(attrs={'class':'nombreformulario','type':'hidden'}),
            'product_id':forms.TextInput(attrs={'class': 'product_idformulario','type':'hidden'})
        }

class SaleOrderForm(forms.ModelForm):

    class Meta:
        model=SaleOrder

        fields=[
            'amount_tax',
            'amount_untaxed',
            'amount_total',
            'name'
        ]
        labels={
            'amount_tax':'Iva acomulada',
            'amount_untaxed':'precio sin IVA',
            'amount_total':'acumulado total',
            'name':'Nombre de la orden'
        }
        widgets={
            'amount_tax':forms.TextInput(attrs={'type': 'hidden'}),
            'amount_untaxed':forms.TextInput(attrs={'type': 'hidden'}),
            'amount_total':forms.TextInput(attrs={'type': 'hidden'}),
            'name':forms.TextInput(attrs={'type': 'hidden'})
        }

class SaleOrderTaxForm(forms.ModelForm):
    class Meta:
        model=SaleOrderTax

        fields=[
            'order_line_id',
        ]