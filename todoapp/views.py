from django.shortcuts import render,redirect
from users.models import *
from users.forms import Taskform
from django.contrib import messages

def todo_list(request):
    task=Tasks.objects.all()
    incomplete=task.filter(complete=False)
    return render(request,"task_list.html",{"task":task,"incomplete":incomplete})

def add_task(request):
    if request.method=="POST":
        form=Taskform(request.POST)
        if form.is_valid():
            user=request.user
            title=form.cleaned_data["title"]
            description=form.cleaned_data["description"]
            complete=form.cleaned_data["complete"]
            tasks=Tasks(user=user,title=title,description=description,complete=complete)
            tasks.save()
            messages.success(request,"Task added sucessfully!!")
        return render(request,"task_add.html",{"form": form})        
    else:        
        form =Taskform()
        return render(request,"task_add.html",{"form": form})
    
def update_task(request,id):
    if request.method =="POST":
        task=Tasks.objects.get(pk=id)
        task.user=request.user
        task.title=request.POST.get("title")
        task.description=request.POST.get("description")
        task.complete=request.POST.get("complete")
        task.save()
        messages.success(request,"Task updated sucessfully!!")
        return render(request,"task_update.html")
    else: 
        task=Tasks.objects.get(pk=id)  
        form=Taskform(instance=task)
        return render(request,"task_update.html",{"form":form,"task":task})

def delete_task(request,id):
    task=Tasks.objects.get(pk=id)
    task.delete()
    return redirect("/home/")

def search_task(request):
    task1=Tasks.objects.filter(title=request.GET["search-area"])
    task=Tasks.objects.all()
    incomplete=task.filter(complete=False)
    return render(request,"task_list.html",{"task":task1,"incomplete":incomplete})
