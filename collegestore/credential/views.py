from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages

# Create your views here.
def login(request):

    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']
        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:

            messages.info( request,"invalid user name or password")
            return redirect('login')


    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            msg=messages.info(request,'Password didnot match')
            return redirect('signup')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
