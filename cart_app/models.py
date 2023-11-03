from django.db import models
from django.contrib.auth.models import User
from products_app.models import product
from customer_app.models import customer_model

# Create your models here.


# class OrderItem(models.Model):
#       id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#       prdct=models.OneToOneField(product,on_delete=models.SET_NULL,null=True)
#       is_ordered=models.BooleanField(default=False)
#       date_added=models.DateField(auto_now=True)
#       date_ordered=models.DateField(null=True)

#       def __str__(self):
#             return self.prdct.name

# class order(models.Model):
#       owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#       is_ordered=models.BooleanField(default=False)
#       items=models.ManyToManyField(OrderItem)
#       date_ordered=models.DateField(auto_now=True)

#       def get_cart_items(self):
#             return self.items.all()
#       def get_cart_total(self):
#             return sum([item.prdct.price for item in self.items.all()])



class cart_item(models.Model):
      item=models.ForeignKey(product,on_delete=models.CASCADE)
      date=models.DateField(auto_now=True)
      quantity=models.IntegerField()
      price=models.FloatField()
      is_ordered=models.BooleanField(default=False)

class cart(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      items=models.ManyToManyField(cart_item)
