from django.db import models
from customer_app.models import customer_model

# Create your models here.

class category(models.Model):
      name=models.CharField(max_length=255)

class product(models.Model):
      name=models.CharField(max_length=255)
      category=models.ForeignKey(category,on_delete=models.CASCADE)
      description=models.CharField(max_length=255)
      price=models.IntegerField()
      count=models.IntegerField()
      photo=models.ImageField(upload_to='products',blank=True)


