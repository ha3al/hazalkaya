from django.http import *
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        ad = request.POST['ad']
        email = request.POST['email']
        return render(request, 'index.html', {"ad": ad, "email": email})
    else:
        return render(request, "index.html")



def deneme(request):
    return render(request, 'deneme.html', locals())
