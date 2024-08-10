from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from .forms import RegisterForm

# Login, Registration, Reset Password

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(email=email,username=username, 
                                            password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request, 'accounts/registration/register.html', context)



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get(
            'next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
            context = {'error':error_message}
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')
    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = '/password_reset/done/'

# account_settings

@login_required
def account_settings_view(request):
    return render(request, 'accounts/account_settings.html')

def account_delete_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')
    return render(request, 'account_delete_confirmation.html')
