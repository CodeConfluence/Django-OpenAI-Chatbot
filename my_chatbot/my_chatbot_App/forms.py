from django import forms
from .models import Agent, Resource, ChatHistory, Message

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'description', 'instructions', 'is_public']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['file']

class ChatHistoryForm(forms.ModelForm):
    class Meta:
        model = ChatHistory
        fields = ['title']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['user_message', 'bot_message']