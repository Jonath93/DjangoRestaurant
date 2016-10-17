from __future__ import unicode_literals
import datetime
from django.utils import timezone 
from django.db import models
from base64 import b64decode

#tabla sale_order
class SaleOrder(models.Model):
    create_date=models.DateTimeField()
    write_uid=models.IntegerField()
    date_order=models.DateTimeField(null=False)
    partner_id=models.IntegerField(null=False)
    amount_tax=models.FloatField()
    procurement_group_id=models.IntegerField()
    amount_untaxed=models.FloatField()
    message_last_post=models.DateTimeField()
    company_id=models.IntegerField()
    state=models.CharField(max_length=200)
    pricelist_id=models.IntegerField(null=False)
    create_uid=models.IntegerField()
    write_date=models.DateTimeField()
    partner_invoice_id=models.IntegerField(null=False)
    user_id=models.IntegerField()
    date_confirm=models.DateField()
    amount_total=models.FloatField()
    name=models.CharField(max_length=200,null=False)
    partner_shipping_id=models.IntegerField(null=False)
    order_policy=models.CharField(max_length=200,null=False)
    picking_policy=models.CharField(max_length=200,null=False)
    warehouse_id=models.IntegerField(null=False)
    shipped=models.BooleanField()

    class Meta:
        db_table = 'sale_order'

class MrpProduction(models.Model):
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
    weight_net=models.FloatField()
    volume=models.IntegerField()
    write_date=models.DateTimeField()
    active=models.BooleanField()
    rental=models.BooleanField()
    name=models.CharField(max_length=200,null=False)
    type=models.CharField(max_length=200,null=False)
    track_all=models.BooleanField()
    track_outgoing=models.BooleanField()
    track_incoming=models.BooleanField()
    sale_delay=models.IntegerField()
    expense_pdt=models.BooleanField()
    income_pdt=models.BooleanField()
    available_in_pos=models.BooleanField()
    to_weight=models.BooleanField()
    track_production=models.BooleanField()
    produce_delay=models.IntegerField()
    file_path=models.CharField(max_length=125)

    class Meta:
        db_table='product_template'

