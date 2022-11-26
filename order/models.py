from django.db import models
from products.models import Product
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
orderstatus = [
    ('Recieved', 'Recieved'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    
]
class Order(models.Model):
    code=models.IntegerField()
    orderstatus=models.CharField(max_length=12,choices=orderstatus)
    total=models.FloatField(null=True,blank=True)
    orderTime=models.DateTimeField(default=timezone.now)
    deliveryTime=models.DateTimeField(null=True,blank=True)
    user= models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='user_order')

    def __str__(self):
         return str(self.code)


class OrderDetail(models.Model):
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True,related_name='orderdetail_order')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True,related_name='product_order')
    quintaty=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField(blank=True,null=True)

    def __str__(self):
         return str(self.order)