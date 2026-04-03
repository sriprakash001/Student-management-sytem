from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate,login,logout

def signup(request):
    context = {
        'error':''
    }
    if request.method == 'POST':
        user_check = User.objects.filter(username=request.POST['username'])
        if len(user_check) > 0:
            context = {
                'error':'* Username altready exist'
            }
            return render(request,'accounts/signup.html',context)
        else:
            new_user = User(first_name = request.POST['first_name'],last_name = request.POST['last_name'] ,username = request.POST['username'])
            new_user.set_password(request.POST['password'])
            new_user.save()
            return redirect('/')
    return render(request,'accounts/signup.html',context)

def login_page(request):
    context = {
        'error':''
    }
    if request.method == 'POST':
        user = authenticate(username = request.POST['username'],password = request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            context = {
                'error':'Invalid Username or Password'
            }
            return render(request,'accounts/login.html',context)
    return render(request,'accounts/login.html',context)

def logout_page(request):
    logout(request)
    return redirect('/')