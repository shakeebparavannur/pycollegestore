from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'index.html')

@login_required
def userdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')
        materials = request.POST.get('materials[]')
        obj = userData(name=name,dob=dob,age=age,gender=gender,mail=email,address=address,phone=phone,
                       department=department,course=course,purpose=purpose,materials=materials)
        obj.save()
        return redirect('/')

    return render(request,'form.html')