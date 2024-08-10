from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registration/register.html', {'form': form})
    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = '/password_reset/done/'

def home_view(request):
    return render(request, 'chatbotApp/home.html')

def profile_view(request):
    return render(request, 'accounts/profile.html')

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
