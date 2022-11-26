from django.contrib import admin
from .models import Order,OrderDetail

# Register your models here.


class Order_admin(admin.ModelAdmin):
    list_display=['code','orderstatus','total','orderTime']



class OrderDetail_admin(admin.ModelAdmin):
    list_display=['order','product','quintaty','price','total']






admin.site.register(Order,Order_admin)
admin.site.register(OrderDetail,OrderDetail_admin)


