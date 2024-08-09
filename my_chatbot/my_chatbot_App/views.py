from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def home(request):
    return render(request, 'chatbotApp/home.html')