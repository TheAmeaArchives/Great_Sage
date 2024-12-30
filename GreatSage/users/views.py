from audioop import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        print("not authenticated")
        return redirect("logins") 
    return redirect("landing")

def logins(request):
   
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request.POST, username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect("landing")
        else:
            form = AuthenticationForm()
            return render(request, "users/logins.html", {'message':'login'})
    return render(request, "users/logins.html", )

def logouts(request):
    logout(request)
    return redirect("logins")

def signup(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logins')
    else:
        form = UserCreationForm()
        
    return render(request, "users/signup.html", {"form": form})
        
