from django import forms
from .models import SaleOrder,SaleOrderLine
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
            'create_date',
            'product_uom',
            'price_unit',
            'product_uom_qty',
            'write_uid',
            'invoiced',
            'create_uid',
            'company_id',
            'name',
            'state',
            'order_partner_id',
            'order_id',
            'discount',
            'write_date',
            'product_id',
            'salesman_id'
        ]
        labels ={
            'product_uos_qty':'cantidad uos',
            'create_date':'Fecha',
            'product_uom':'product uom',
            'price_unit':'precio Unitario',
            'product_uom_qty':'Cantidad',
            'write_uid':'write_uid',
            'invoiced':'invoiced',
            'create_uid':'create_uid',
            'company_id':'compania',
            'name':'nombre',
            'state':'estado',
            'order_partner_id':'cliente',
            'order_id':'orden id',
            'discount':'descuento',
            'write_date':'fecha escritura',
            'product_id':'producto id',
            'salesman_id':'vendedor id'
        }
        widgets = {
            'product_uos_qty':forms.TextInput(),
            'create_date':forms.DateInput(),
            'product_uom':forms.TextInput(),
            'price_unit':forms.TextInput(),
            'product_uom_qty':forms.TextInput(),
            'name':forms.TextInput(),
            'state':forms.TextInput(),
            'order_partner_id':forms.TextInput(),
            'order_id':forms.TextInput(),
            'discount':forms.TextInput(),
            'write_date':forms.DateInput(),
            'product_id':forms.TextInput()
        }

class SaleOrderForm(forms.ModelForm):
    class Meta:
        model=SaleOrder

        fields=[
            'create_date',
            'write_uid',
            'date_order',
            'partner_id',
            'amount_tax',
            'procurement_group_id',
            'amount_untaxed',
            'company_id',
            'state',
            'pricelist_id',
            'create_uid',
            'write_date',
            'partner_invoice_id',
            'user_id',
            'date_confirm',
            'amount_total',
            'name',
            'partner_shipping_id',
            'order_policy',
            'picking_policy',
            'warehouse_id',
            'shipped'
        ]
        labels={
            'create_date':'fecha Creacion',
            'write_uid':'id escritura',
            'date_order':'fecha de orden',
            'partner_id':'id de cliente',
            'amount_tax':'Iva acomulada',
            'procurement_group_id':'id grupo',
            'amount_untaxed':'precio sin IVA',
            'company_id':'compania id',
            'state':'estado',
            'pricelist_id':'lista de precio id',
            'create_uid':'id creacion',
            'write_date':'fecha de escritura',
            'partner_invoice_id':'socio id',
            'user_id':'user id',
            'date_confirm':'fecha de confirmacion',
            'amount_total':'acumulado total',
            'name':'nombre',
            'partner_shipping_id':'socio id',
            'order_policy':'orden de politica',
            'picking_policy':'politica',
            'warehouse_id':'almacen id',
            'shipped':'Enviado'
        }
        widgets = {
            'create_date':forms.DateTimeInput(),
            'write_uid':forms.NumberInput(),
            'date_order':forms.DateTimeInput(),
            'partner_id':forms.NumberInput(),
            'amount_tax':forms.NumberInput(),
            'procurement_group_id':forms.NumberInput(),
            'amount_untaxed':forms.NumberInput(),
            'company_id':forms.NumberInput(),
            'state':forms.TextInput(),
            'pricelist_id':forms.NumberInput(),
            'create_uid':forms.NumberInput(),
            'write_date':forms.DateTimeInput(),
            'partner_invoice_id':forms.NumberInput(),
            'user_id':forms.NumberInput(),
            'date_confirm':forms.DateInput(),
            'amount_total':forms.NumberInput(),
            'name':forms.TextInput(),
            'partner_shipping_id':forms.NumberInput(),
            'order_policy':forms.TextInput(),
            'picking_policy':forms.TextInput(),
            'warehouse_id':forms.NumberInput(),
            'shipped':forms.TextInput()
        }