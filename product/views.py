from django.shortcuts import render ,redirect
from .models import products ,cart
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
def product(req):
    productss=products.objects.all()

    return render(req,"product/productss.html",locals())


def add_to_cart(request,id):
        if request.user.is_authenticated:
            prod=products.objects.get(id=id)
            if prod:
                cart_prod=cart.objects.filter(prod=prod)
                if cart_prod:
                    for i in cart_prod:
                        i.quantity+=1
                        i.save()
                        na=i.prod
                        return redirect(request.META['HTTP_REFERER'])
                else:
                        add_cart=cart.objects.create(user=request.user,prod=prod)
                        add_cart.save()
                        return redirect(request.META['HTTP_REFERER'])
        else:
            messages.warning(request,"LOG_IN TO ADD TO CART")
            return redirect('sing_in')
                    
                