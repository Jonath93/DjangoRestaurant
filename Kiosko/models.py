from __future__ import unicode_literals
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone 
from django.db import models
from base64 import b64decode
from datetime import datetime,date


#tabla sale_order
class SaleOrder(models.Model):
    create_date=models.DateTimeField(default=datetime.now, blank=True)
    write_uid=models.IntegerField(default=1)
    date_order=models.DateTimeField(default=datetime.now, blank=True,null=False)
    partner_id=models.IntegerField(default=7)
    amount_tax=models.FloatField()
    amount_untaxed=models.FloatField()
    company_id=models.IntegerField(default=1)
    state=models.CharField(max_length=200,default="manual")
    pricelist_id=models.IntegerField(default=1,null=False)
    create_uid=models.IntegerField(default=1)
    write_date=models.DateTimeField(default=datetime.now, blank=True)
    partner_invoice_id=models.IntegerField(null=False,default=7)
    user_id=models.IntegerField(default=1)
    amount_total=models.FloatField()
    name=models.CharField(max_length=100)
    partner_shipping_id=models.IntegerField(null=False, default=7)
    order_policy=models.CharField(max_length=200, null=False, default="manual")
    picking_policy=models.CharField(max_length=200, null=False, default="direct")
    warehouse_id=models.IntegerField(null=False, default=1)
    
    class Meta:
        db_table = 'sale_order'

class SaleOrderLine(models.Model):
    product_uos_qty=models.FloatField()
    create_date=models.DateTimeField(default=datetime.now, blank=True)
    product_uom=models.IntegerField(null=False,default=1)
    sequence=models.IntegerField(default=11)
    price_unit=models.FloatField(null=False)
    product_uom_qty=models.FloatField(null=False)
    write_uid=models.IntegerField(default=1)
    invoiced=models.BooleanField(default=False)
    create_uid=models.IntegerField(default=1)
    company_id=models.IntegerField(default=1)
    name=models.CharField(max_length=900,null=False)
    delay=models.IntegerField(default=0)
    state=models.CharField(max_length=200,null=False,default='confirmed')
    order_partner_id=models.IntegerField(null=False,default=7)
    order_id=models.IntegerField(null=False)
    discount=models.FloatField()
    write_date=models.DateTimeField(default=datetime.now, blank=True)
    product_id=models.IntegerField()
    salesman_id=models.IntegerField(default=1)

    class Meta:
        db_table='sale_order_line'


class SaleOrderTax(models.Model):
    order_line_id=models.IntegerField()
    tax_id=models.IntegerField(default=3)

    class Meta:
        db_table='sale_order_tax'


class MrpProduction(models.Model):
    id=models.IntegerField(primary_key=True)
    create_date=models.DateField()
    product_uom=models.IntegerField()
    product_uos_qty=models.FloatField()
    write_uid=models.IntegerField()
    product_qty=models.FloatField()
    create_uid=models.IntegerField()
    user_id=models.IntegerField()
    location_src_id=models.IntegerField()
    cycle_total=models.FloatField()
    company_id=models.IntegerField()
    priority=models.IntegerField()
    state=models.CharField(max_length=200)
    bom_id=models.IntegerField()
    write_date=models.DateTimeField()
    name=models.CharField(max_length=200)
    product_id=models.IntegerField()
    date_planned=models.DateTimeField()
    ready_production=models.BooleanField()
    hour_total=models.FloatField()
    location_dest_id=models.IntegerField()
    
    class Meta:
        db_table = 'mrp_production'

class ResUsers(models.Model):
    id=models.IntegerField(primary_key=True)
    active=models.BooleanField()
    login=models.CharField(max_length=64)
    password=models.CharField(max_length=200)
    company_id=models.IntegerField()
    partner_id=models.IntegerField()
    create_uid=models.IntegerField()
    login_date=models.DateField()
    write_uid=models.IntegerField()
    write_date=models.DateTimeField()
    signature=models.TextField()
    password_crypt=models.CharField(max_length=600)
    alias_id=models.IntegerField()
    display_group_suggestions=models.BooleanField()
    share=models.BooleanField()
    pos_config=models.IntegerField()

    class Meta:
        db_table='res_users'

class ProductTemplate(models.Model):
    id=models.IntegerField(primary_key=True)
    list_price=models.FloatField()
    weight=models.FloatField()
    color=models.IntegerField()
    image=models.BinaryField()
    image_small=models.BinaryField()
    write_uid=models.IntegerField()
    mes_type=models.CharField(max_length=200)
    uom_id=models.IntegerField(null=False)
    create_date=models.DateTimeField()
    uos_coeff=models.FloatField()
    create_uid=models.IntegerField()
    sale_ok=models.BooleanField()
    categ_id=models.IntegerField(null=False)
    company_id=models.IntegerField()
    uom_po_id=models.IntegerField(null=False)
    description=models.CharField(max_length=9000)
    weight_net=models.FloatField()
    volume=models.IntegerField()
    write_date=models.DateTimeField()
    active=models.BooleanField()
    rental=models.BooleanField()
    name=models.CharField(max_length=200, null=False)
    type=models.CharField(max_length=200, null=False)
    track_all=models.BooleanField()
    track_outgoing=models.BooleanField()
    track_incoming=models.BooleanField()
    sale_delay=models.IntegerField()
    expense_pdt=models.BooleanField()
    pos_categ_id=models.IntegerField()
    income_pdt=models.BooleanField()
    available_in_pos=models.BooleanField()
    to_weight=models.BooleanField()
    track_production=models.BooleanField()
    produce_delay=models.IntegerField()
    file_path=models.CharField(max_length=125)

    class Meta:
        db_table='product_template'

class PosCategory(models.Model):
    id=models.IntegerField(primary_key=True)
    create_uid=models.IntegerField()
    create_date=models.DateTimeField()
    name=models.CharField(max_length=200)
    sequence=models.IntegerField()
    image=models.BinaryField()
    write_uid=models.IntegerField()
    write_date=models.DateTimeField()

    class Meta:
        db_table='pos_category'

class ResPartner(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    
    class Meta:
        db_table='res_partner'

