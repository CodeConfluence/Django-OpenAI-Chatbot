from django import forms
from .models import Agent, Resource

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'description', 'instructions', 'is_public']

class ResourceForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(), required=False)

    class Meta:
        model = Resource
        fields = ['files']