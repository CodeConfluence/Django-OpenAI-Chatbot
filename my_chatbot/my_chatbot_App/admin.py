from django.contrib import admin
from .models import Agent, Resource, ChatHistory, Message

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator', 'is_public', 'description', 'user_defined_instructions', 'created_at')
    search_fields = ('name', 'creator__username')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'agent', 'file', 'uploaded_at')
    search_fields = ('title', 'agent__name')

@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('agent', 'title')
    search_fields = ('title', 'agent__name')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('history', 'user_message', 'bot_message', 'created_at')
    search_fields = ('history__title',)