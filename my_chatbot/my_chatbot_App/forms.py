from django import forms
from .models import Agent  # Assuming you have an Agent model

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'description']