from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout






def sing_up(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if password==password2:
                if User.objects.filter(email=email).exists():
                     messages.warning(request, "Email is Allready Taken !!!")
                elif User.objects.filter(username=username).exists():
                     messages.warning(request,"This User name Is Allready Taken !!! ")
                else:      
                    user=User.objects.create(first_name=first_name,last_name=last_name,email=email,username=username)
                    user.set_password(password)
                    user.save()
                    messages.success(request, "Registration Successful")
                    return redirect(sing_in)       
        else:
            messages.warning(request, "  Password not Matched  ")
            

    return render(request,'account/sing_up.html',locals())



def sing_in(request): 
    if request.user.is_authenticated:
         return redirect('index') 
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
             print(user)
            
             login(request,user)
             
             messages.success(request,"User Loged in SuccessFull !!!")
             return redirect('index')
        else:
             messages.warning(request,"Plase create A user First ")
             return redirect('sing_up')
        
    return render(request,'account/log_in.html')

def sing_out(request):
        logout(request)
        return redirect('sing_in')