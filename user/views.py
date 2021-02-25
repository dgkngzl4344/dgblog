from django.shortcuts import render , redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout





def register(request):
    form = RegisterForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newuser=User(username = username)
        newuser.set_password(password)
        newuser.save()
        messages.success(request,"başarıyla kayıt oldunuz")
        return redirect("index")
    return render(request,"register.html",context) 
def loginuser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user = authenticate(username = username , password = password)
        if user is None:
            messages.warning(request,"Kullanıcı adı veya parola hatalı")
            return render(request,"login.html",context)

        messages.success(request,"başarıyla giriş yaptın !!")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)    

def logoutUser(request):
    logout(request)
    messages.success(request,"başarıyla çıkış yaptınız")
    return redirect("index")