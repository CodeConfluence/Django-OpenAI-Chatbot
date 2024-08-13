from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('home/', views.home_view, name='home'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.account_update_view, name='account_update'),
    path('profile/upload-image/', views.profile_image_upload, name='profile_image_upload'),
    path('profile/update/confirmation', views.account_update_confirmation_view, name='account_update_confirmation'),
    path('profile/account_delete', views.account_delete_view, name='account_delete'),
    path('agents/', views.agent_list_view, name='agent_list'), # list of agents
    path('agents/create/', views.create_agent_view, name='create_agent'), # create a new agent
    path('agents/<int:agent_id>/', views.agent_detail_view, name='agent_detail'), # view agent details
    path('agents/<int:agent_id>/edit/', views.update_agent_view, name='edit_agent'), # update agent details
    path('agents/<int:agent_id>/delete/', views.delete_agent_view, name='delete_agent'), # delete agent
    path('agents/selection/', views.agent_selection_view, name='agent_selection'), # where the user whichever agent they're going to use
    path('generate-content/<str:agent_name>/', views.generate_content_view, name='generate_content'),
    # path('agents/<int:agent_id>/chat/', views.chat_interface_view, name='agent_chat'), still need to work on this
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)