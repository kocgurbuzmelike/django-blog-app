from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

#Kayıt ol
def register(request):
    if request.method=="POST":

        form = RegisterForm(request.POST)

        if form.is_valid(): #CLEAN METOODU ÇAĞIRILIYOR
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            newUser=User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            messages.success(request,"Başarıyla kayıt oldunuz.")
            return redirect("index")
        context={
            "form" : form
        }

        return render(request,"register.html", context)

    else:
        form=RegisterForm()
        context={
            "form" : form
        }
        return render(request,"register.html", context)

 


#Giriş
def loginUser(request):

    form=LoginForm(request.POST or None)
    context={
        "form" : form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username, password=password)

        if user is None:
            messages.info(request,"Kullanıcı adı veya parola hatalı.")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla giriş yaptınız.")
        login(request,user)
        return redirect("index")
    
    return render(request,"login.html",context)

#Çıkış
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı.")
    return redirect("index")