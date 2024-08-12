from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, LoginView, LogoutView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Agent
from .forms import AgentForm

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            return render(request, 'accounts/registration/register.html')

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/registration/register.html')

        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/registration/register.html')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            send_mail(
                'Welcome to SocialBrain.ai',
                'Thank you for registering with SocialBrain.ai!',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return redirect('home')
        except ValidationError as e:
            return render(request, 'accounts/registration/register.html')

    return render(request, 'accounts/registration/register.html')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name)


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/logout.html'
    next_page = reverse_lazy('login')


class CustomPasswordResetView(LoginRequiredMixin, PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = '/password_reset/done/'

@login_required
def home_view(request):
    return render(request, 'chatbotApp/home.html')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required
def account_settings_view(request):
    return render(request, 'accounts/account_settings.html')

@login_required
def account_delete_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('home')
    return render(request, 'accounts/account_delete_confirmation.html')

# GOOGLE VERTEX AI (SHOULD PROBABLY CREATE A SEPERATE VIEW FILE)

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.cloud import aiplatform

# Initialize the Vertex AI client
PROJECT_ID = "verdant-coyote-432222-u6"
LOCATION = "us-central1"  
MODEL_NAME = "projects/{}/locations/{}/models/{}".format(PROJECT_ID, LOCATION, "gemini-1.5-flash-001")

aiplatform.init(project=PROJECT_ID, location=LOCATION)
endpoint = aiplatform.Endpoint(endpoint_name=MODEL_NAME)

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')

        if not user_message:
            return JsonResponse({"error": "No message provided"}, status=400)

        request_payload = {
            "instances": [
                {"input_text": user_message}
            ]
        }

        response = endpoint.predict(requests=request_payload)
        chatbot_response = response.predictions[0]['output_text']

        return JsonResponse({"response": chatbot_response})

    return render(request, 'chat.html')

@login_required
def create_agent_view(request): # create a new agent
   if request.method == 'POST':
       form = AgentForm(request.POST, request.FILES)
       if form.is_valid(): # save agent and go to agent list
           agent = form.save(commit=False)
           agent.creator = request.user
           agent.save()
           for f in request.FILES.getlist('resources'):
               agent.resources.save(f.name, f)
           return redirect('agent_list') # go to agent list
   else:
       form = AgentForm()
   return render(request, 'agents/create_agent.html', {'form': form}) # go to create agent page

@login_required
def agent_list_view(request): # getting list of agents
   agents = Agent.objects.filter(creator=request.user)
   return render(request, 'agents/agent_list.html', {'agents': agents}) # render agent list

@login_required
def agent_detail_view(request, agent_id): # for viewing agent details
   agent = get_object_or_404(Agent, id=agent_id, creator=request.user)
   return render(request, 'agents/agent_detail.html', {'agent': agent}) # render agent details

@login_required
def update_agent_view(request, agent_id): # update agent details
   agent = get_object_or_404(Agent, id=agent_id, creator=request.user)
   if request.method == 'POST': # will save agent
       form = AgentForm(request.POST, instance=agent)
       if form.is_valid():
           form.save()
           return redirect('agent_list')
   else: # go to the form
       form = AgentForm(instance=agent)
   return render(request, 'agents/update_agent.html', {'form': form, 'agent': agent})

@login_required
def delete_agent_view(request, agent_id):
   agent = get_object_or_404(Agent, id=agent_id, creator=request.user)
   if request.method == 'POST': # will delete agent
       agent.delete()
       return redirect('agent_list')
   return render(request, 'agents/delete_agent.html', {'agent': agent}) # go back to the delete agent page

@login_required
def agent_selection_view(request): # where the user selects which agent they're going to use
   user_agents = Agent.objects.filter(creator=request.user)
   public_agents = Agent.objects.filter(is_public=True).exclude(creator=request.user)
   return render(request, 'agents/agent_selection.html', { # go to the agent select page
       'user_agents': user_agents,
       'public_agents': public_agents,
   })

# @login_required
# def chat_interface_view(request, agent_id):
#   agent = get_object_or_404(Agent, id=agent_id)
   #return render(request, 'chatbotApp/chat_interface.html', {'agent': agent})
#need to work on this
