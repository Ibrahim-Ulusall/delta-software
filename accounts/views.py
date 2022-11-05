from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request,'accounts/index.html')

def register(request):
    return render(request,'accounts/register.html')