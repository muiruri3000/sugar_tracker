from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



def login_view(request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST or None)
        if request.method=='POST' and form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'login/login-page.html',{'form':form})

@login_required
def home(request):
    return render(request,'login/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')