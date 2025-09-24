from django.shortcuts import render,redirect
from .forms import SchoolAdminRegistrationForm,SchoolAdminLoginForm
# Create your views here.

def school_admin_register(request):
    if request.method=='POST':
        form=SchoolAdminRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        context={
            'form':form
        }   
        return render(request,'accounts/register.html',context)
    form=SchoolAdminRegistrationForm()
    context ={
        'form':form
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method=='POST':
        form=SchoolAdminLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:home')
        context={
            'form':form
        }
        return render(request,'accounts/login.html',context)
    form=SchoolAdminLoginForm()
    context={
        'form':form
    }
    return render(request,'accounts/login.html',context)