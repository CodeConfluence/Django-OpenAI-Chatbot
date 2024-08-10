from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agent(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agents')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Agent: {self.name}"

class Resource(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='resources/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Interaction(models.Model):
    #To be implemented
    pass
class Feedback(models.Model):
    #To be implemented
    pass
class Analytics(models.Model):
    #To be implemented
    pass