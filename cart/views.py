from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        redirect('cart')
    else:
        messages.warning(request,"PLEASE  LOG IN FIRST ")
        return redirect('sing_in')
    
    return render(request,'cart/cart.html')