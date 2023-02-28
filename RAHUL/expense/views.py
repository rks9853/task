from django.shortcuts import render, redirect
from .models import Expense_track
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def login(request):
    if request.method=='POST':
          username=request.POST.get('username')
          password=request.POST.get('password')
          user= authenticate(username=username,password=password)
          if user is not None:
               auth.login(request,user)
               return redirect("home")
    else:
        return render(request, "login.html")      
    return render(request, "login.html")



def logout_page(request):
    logout(request)
    return redirect("login")



def delete(request,pk):
    delt=Expense_track.objects.get(pk=pk)
    delt.delete()
    return redirect("home")
    


@login_required(login_url='login')
def index(request):
    print(request.user.id)
    data = Expense_track.objects.all()
    ctx={"data":data}
    return render (request,'index.html', ctx)




def credit(request):
    if request.method=="POST":
        c_am = request.POST.get("amount")
        des = request.POST.get("description")
        dt = request.POST.get("date")
        if c_am and des and dt:
                b = Expense_track(description=des, credit=c_am, date=dt)
                b.save()
    return redirect("home")



def debit(request):
    if request.method=="POST":
        d_am = request.POST.get("amount")
        des = request.POST.get("description")
        dt = request.POST.get("date")
        if d_am and des and dt:
                b = Expense_track(description=des, debit=d_am, date=dt)
                b.save()
    return redirect("home")
