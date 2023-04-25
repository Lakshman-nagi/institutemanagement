from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache

from StudentApp.models import City, Course, Student
from django.contrib import messages

# Create your views here
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def reg_fun(request):
    return render(request, 'register.html', {'data': ''})


def regdata_fun(request):
    user_name = request.POST['tbuser']
    user_email = request.POST['tbemail']
    user_pswd = request.POST['tbpswrd']

    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, 'register.html', {'data': 'username,email and password is already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name, email=user_email, password=user_pswd)
        u1.save()
        return redirect('log')


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_fun(request):
    return render(request, 'login.html', {'data': ''})

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def logdata_fun(request):
    user_name = request.POST['tbuser']
    user_pswrd = request.POST['tbpswrd']
    user1 = authenticate(username=user_name, password=user_pswrd)
    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request, 'login.html', {'data': 'user is not superuser','res':False})
    else:
        return render(request, 'login.html', {'data': 'enter proper username and password','res':True})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def home_fun(request):
    return render(request, 'home.html')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def addstudent_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request, 'addstudent.html', {'city_data': city, 'course_data': course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def readdata_fun(request):
    s1 = Student()
    s1.Std_Name = request.POST['tbname']
    s1.Std_Age = int(request.POST['tbage'])
    s1.Std_Phno = int(request.POST['tbnum'])
    s1.Std_City = City.objects.get(City_Name=request.POST['ddlcity'])
    s1.Std_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
    if not Student.objects.filter(Q(Std_Phno=s1.Std_Phno)).exists():
        s1.save()
        messages.success(request,' added successfully ')
    else:
        messages.success(request,'it is already exists')
    return redirect('add')
@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def studentdsply_fun(request):
    s1 = Student.objects.all()
    return render(request,'display.html', {'data': s1})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def update_fun(request,id):
    s1=Student.objects.get(id=id)
    city=City.objects.all()
    course=Course.objects.all()
    if request.method=='POST':
        s1.Std_Name=request.POST['tbname']
        s1.Std_Age=int(request.POST['tbage'])
        s1.Std_Phno=(request.POST['tbnum'])
        s1.Std_City=City.objects.get(City_Name=request.POST['ddlcity'])
        s1.Std_Course=Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.save()

        return redirect('studentdisplay')
    return render(request,'update.html',{'data':s1,'city_data':city,'course_data':course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def delete_fun(request,id):
    s1=Student.objects.get(id=id)
    s1.delete()
    return redirect('studentdisplay')

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def logout_fun(request):
    logout(request)
    return redirect('log')