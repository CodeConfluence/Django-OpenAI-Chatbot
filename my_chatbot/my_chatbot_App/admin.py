from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Agent, Resource

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator', 'is_public', 'description', 'instructions', 'created_at')
    search_fields = ('name', 'creator__username')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'agent', 'file', 'uploaded_at')
    search_fields = ('title', 'agent__name')