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

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['passowrd']
        re_password = request.POST['re-password']

        userInput = [firstname,lastname,username,email,password,re_password]

        for userinput in userInput:
            if userinput == '':
                return render(request,'accounts/register.html',{
                    'ValueError':'Tüm Alanlar Doldurulmalıdır.'
                })
        if '@gmail.com' not in email or '@hotmail.com' not in email:
            return render(request,'accounts/register.html',{
                'FormatError':'Lütfen İstenilen Formatta mail adresi giriniz.'
            })    
        if password != re_password:
            return render(request,'accounts/register.html',{
                'EqualsError':'Parolalar Uyuşmuyor.'
            })
        else:
            pass


    return render(request,'accounts/register.html')