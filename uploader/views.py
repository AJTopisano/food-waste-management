from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def loggin(request):
    return render(request,'uploader/login1.html')

def registerpage(request):
    form = CustomUserForm()
    if request.user.is_authenticated:
        messages.info(request,"You are already Registered")
        return redirect('/')
    else:
        if request.method == 'POST':
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Registered Successfully")
                return redirect('login')
            print(form.errors)
        context = {'form':form}

        return render(request,'uploader/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.info(request,"You are already logged in")
        return redirect('/')
    else:
        if request.method == 'POST':
            loginusername = request.POST.get('username')
            loginpassword = request.POST.get('password')

            user = authenticate(request,username=loginusername, password=loginpassword)

            if user is not None:
                print("kenlo")
                login(request,user)
                messages.success(request,'Logged in Succeddfully')
                return redirect('posting')
            else:
                print("henlo")
                messages.success(request,'Incorrect Credentials')

        return render(request,'uploader/login.html')

def logoutpage(request):
    logout(request)
    messages.info(request,"Logged out successfully")
    return redirect('homee')   # redirec('/') means redirect to home page

def home(request):
    return render(request,'uploader/home.html')

def posting(request):
    form = fpost.objects.all()
    context = {'form':form}
    return render(request,'uploader/main.html',context)

def viewpost(request,pk): #pk = Primary Key
    post = fpost.objects.get(id=pk)
    context = {'post':post}
    return render(request,'uploader/viewpost.html',context)

def addpost(request):
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Post added Successfully")
            return redirect('posting')

    context = {'form':form}
    return render(request,'uploader/addform.html',context)

def deleteblog(request,pk):
    form = fpost.objects.get(id=pk)
    form.delete()
    messages.info(request,"Post Deleted Successfully")
    return redirect('posting')
def homee(request):
    return render(request,'uploader/home.html')

