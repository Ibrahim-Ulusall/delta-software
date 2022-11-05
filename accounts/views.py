from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def login(request):
    
    return render(request,'accounts/index.html')    

def register(request):
    return render(request,'accounts/register.html')