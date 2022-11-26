from django.shortcuts import render

from . models import Order

# Create your views here.

def order_list(request):

    object=Order.objects.all()
    return render (request,'orderlist.html',{'order':object})
