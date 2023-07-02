from django.shortcuts import render,redirect
from .forms import Regform,loginform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def reg(request):
    if request.method=="POST":
        form=Regform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User account has been created sucessfully!!")
        return render (request,"register.html",{"form":form})
    else:
        form= Regform()
        return render (request,"register.html",{"form":form})
                
def signin(request):
    if request.method =="POST":
        form=loginform(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data["username"]
            passw=form.cleaned_data["password"]
            user=authenticate(username=uname,password=passw)
            if user is not None:
                login(request,user)
                messages.success(request,"logeed in successfully!!!")
            return redirect("/home/")
        return render (request,"login.html",{"form":form})
    else:
        form=loginform()
        return render (request,"login.html",{"form":form})
    
def signout(request):
    logout(request)
    return redirect("/user/signin/")