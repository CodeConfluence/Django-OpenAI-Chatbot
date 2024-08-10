from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('account/settings/', views.account_settings_view, name='account_settings'),
    path('account/settings/password_change/', auth_views.PasswordChangeView.as_view(), 
         name='password_change'),
    path('account/settings/password_change/done', auth_views.PasswordChangeDoneView.as_view(), 
         name='password_change_done.html'),
    path('account/settings/account_delete', views.account_delete_view, 
         name='account_delete'),
]