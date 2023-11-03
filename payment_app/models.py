from django.db import models
from cart_app.models import cart_item
# Create your models here.

class payment(models.Model):
      order_item=models.ForeignKey(cart_item,on_delete=models.CASCADE,null=True)
      order_id=models.CharField(max_length=100,null=True)
      payment_id=models.CharField(max_length=100,null=True)
      paid=models.BooleanField(default=False)