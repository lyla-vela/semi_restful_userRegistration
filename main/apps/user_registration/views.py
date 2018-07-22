from django.shortcuts import render, HttpResponse, redirect
from .models import *  # the index function is called when root is visited
def index(request):
  return redirect('/all_userx')

def all_userx(request):
    context = {
        'all_users':Users.objects.all(),
    }
    return render(request,"user_registration/index.html",context)

def new_registration(request):
  if request.method =="POST":
    user = Users.objects.create(first_name=request.POST['first_name'],
       last_name=request.POST['last_name'],
       email=request.POST['email'])
    user.save()
    return redirect('/')
  else:
    return render(request, 'user_registration/new_user.html')

def edit(request,id):
  context={
        'user':Users.objects.get(id=id)
  }
  return render(request,'user_registration/edit_user.html',context)

def update(request, id):
  if request.method=="POST":
    user=Users.objects.get(id=int(request.POST['hdnID']))
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    response=HttpResponse("User was succesfully updated")
    return redirect(request, 'user_registration/edit_user.html', response)
  else:
    
    return redirect('/')
  # messages.success(request, "User's data were successfully updated")
  # redirect to a success route
    
def show(request,id):
    context={
        'user':Users.objects.get(id=id)
    }
    return render(request,'user_registration/show.html',context)
def destroy(request,id):
    user=Users.objects.get(id=id)
    user.delete()
    return redirect('/all_userx')
  
  
  
