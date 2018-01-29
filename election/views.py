from django.http import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home(request):
    if request.method == 'POST':
        ad = request.POST['ad']
        email = request.POST['email']
        return render(request, 'index.html', {"ad": ad, "email": email})
    else:
        print(request.user.email)
        return render(request, "index.html")



def deneme(request):
    return render(request, 'deneme.html', locals())

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username= email, password= password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login_view.html")

    return render(request, "login_view.html")


