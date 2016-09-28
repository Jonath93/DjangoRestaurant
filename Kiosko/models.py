from __future__ import unicode_literals
import datetime
from django.utils import timezone 
from django.db import models

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
    commitment_date=models.DateTimeField()

    class Meta:
        db_table = 'sale_order'
        