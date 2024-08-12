from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('account/settings/', views.account_settings_view, name='account_settings'),
    path('account/settings/password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), 
         name='password_change'),
    path('account/settings/password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), 
         name='password_change_done'),
    path('account/settings/account_delete', views.account_delete_view, 
         name='account_delete'),
    path('profile/', views.profile_view, name='profile'),
]