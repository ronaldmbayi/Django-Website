
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


# Create your views here.


def dashboard(request):
    return render(request, 'create_account/dashboard.html')


def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = authenticate(username=username, password=password, email=email)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "create_account/signup.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "create_account/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        Email = request.POST.get("Email")
        confirm_password = request.POST.get("confirm_password")

        myuser = User.objects.create_user(username, Email, confirm_password)
        myuser.save()
        return redirect("signin")
    return render(request, "create_account/signup.html")


def signout(request):
    logout(request)
    return render(request, "create_account/signin.html", {
        "message": "Logout out"
    })
