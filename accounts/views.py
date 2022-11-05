from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

# Create your views here.


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/index.html',{
                'hata':'Kullanıcı adi veya parola hatalı!'
            })


    return render(request,'accounts/index.html')    

def register(request):
    return render(request,'accounts/register.html')