from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
# Create your views here.

def home(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user  = form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('dashboard')
    context = {'form':form}
    return render(request,'index.html',context)


def dashboard(request):
    # user = User.objects.all()
    return render(request,'dashboard.html')


def loginhandle(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
    form = AuthenticationForm()
    return render(request,'login.html',context={'form':form})


def signout(request):
    logout(request)
    return redirect('home')