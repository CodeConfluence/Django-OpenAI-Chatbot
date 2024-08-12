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
    
    path('agents/', views.agent_list_view, name='agent_list'), # list of agents
    path('agents/create/', views.create_agent_view, name='create_agent'), # create a new agent
    path('agents/<int:agent_id>/', views.agent_detail_view, name='agent_detail'), # view agent details
    path('agents/<int:agent_id>/edit/', views.update_agent_view, name='edit_agent'), # update agent details
    path('agents/<int:agent_id>/delete/', views.delete_agent_view, name='delete_agent'), # delete agent
    path('agents/selection/', views.agent_selection_view, name='agent_selection'), # where the user whichever agent they're going to use

    # path('agents/<int:agent_id>/chat/', views.chat_interface_view, name='agent_chat'), still need to work on this
]