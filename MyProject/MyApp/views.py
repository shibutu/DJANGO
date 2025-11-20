from django.shortcuts import render,redirect,get_object_or_404
from . forms import StudentForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import *
from . forms import *
# Create your views here.
def Home(request):
    return render(request,'MyApp/index.html')
def stdForm(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form=StudentForm()
        context={'form':form}
    return render(request,'MyApp/stdForm.html',context)

#saving data from user customised HTML forms
def registstd(request):
    if request.method=='POST':
       firstName=request.POST['fname']
       lastName=request.POST['lname']
       email=request.POST['email']
       age=request.POST['age']
       regNo=request.POST['regNo']
       std=student(firstName=firstName,secondName=lastName,email=email,age=age,regNo=regNo)
       std.save()
       return HttpResponse('sucess')
    else:
        return render(request,'MyApp/student.html') 
def retrievestd(request):
    std_data=student.objects.all()
    context={'std_data':std_data}
    return render(request,'MyApp/std_details.html',context)
def updatestd(request,pk):
    Student=get_object_or_404(student,pk=pk)
    if request.method=='POST':
        new_fname=request.POST.get('fname')
        new_lname=request.POST.get('lname')
        new_email=request.Post.get('email')
        new_age=request.POST.get('age')
        new_regNo=request.POST.get('regNo')
        student.fname=new_fname
        student.lname=new_lname
        student.email=new_email
        student.age=new_age
        student.regNo=new_regNo
        student.save()
        return redirect('fetch_std')  
    else:
        context={'student':student}
        return render(request,'MyApp/updatesstd.html context')
#deleting
def deletestd(request,pk):
    del_std=get_object_or_404(student,pk=pk)
    if request.method=='POST':
        del_std.delete()
        return redirect('fetch_std')
    
    return render(request,'MyApp/deletestd.html')
#user authentication  
def userRegistration(request):
    if request.method=='POST':
        form=customUser(request.POST)
        if form.is_valid():
         form.save()
        return redirect('login')
    else:
        form=customUser()
    context={'form':form}
    return render(request,'MyApp/regist.html',context)
#login
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('fetch_std')
    else:
        return render(request,'MyApp/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')