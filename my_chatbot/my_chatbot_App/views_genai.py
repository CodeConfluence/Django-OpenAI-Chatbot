import vertexai
from vertexai.preview import caching
from vertexai.generative_models import GenerativeModel, Part, Content
import datetime
import os
import logging

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config

from .models import Agent, ChatHistory, Message

logger = logging.getLogger(__name__)

@csrf_exempt
def generate_content_view(request, agent_name):
    """
    Generate AI content using Vertex AI with context caching.
    Caches the agent's knowledge base PDF for efficient repeated queries.
    """
    agent = get_object_or_404(Agent, name__iexact=agent_name, creator=request.user)

    try:
        vertexai.init(project=config('GOOGLE_PROJECT_ID'), location=config('GOOGLE_CLOUD_REGION', default='us-central1'))
    except Exception as e:
        logger.warning(f"Vertex AI initialization: {e}")

    cached_content = None
    try:
        # Check if a cache ID already exists for this agent
        if agent.cache_id:
            try:
                cached_content = caching.CachedContent(cached_content_name=agent.cache_id)
                logger.info(f"Using existing cache for agent '{agent.name}': {agent.cache_id}")
            except Exception as e:
                logger.warning(f"Could not retrieve cache {agent.cache_id}, creating new one: {e}")
                agent.cache_id = None
                
        # If no valid cache exists, create one
        if not agent.cache_id:
            logger.info(f"Creating new cache for agent '{agent.name}'...")
            directory_path = f"media/uploads/agents/{agent.id}/"
            
            try:
                files = os.listdir(directory_path)
                if not files:
                    return JsonResponse({"error": "No knowledge base file found for this agent."}, status=400)
                
                # Get the first PDF file
                pdf_file = next((f for f in files if f.endswith('.pdf')), None)
                
                if not pdf_file:
                    return JsonResponse({"error": "No PDF file found for this agent."}, status=400)
                
                file_path = os.path.join(directory_path, pdf_file)
                
                # Read the PDF file and create a Part
                with open(file_path, 'rb') as f:
                    pdf_data = f.read()
                
                knowledge_base_file_part = Part.from_data(data=pdf_data, mime_type="application/pdf")

                cached_content = caching.CachedContent.create(
                    model_name="gemini-1.5-pro-001",
                    system_instruction=agent.instructions,
                    contents=[knowledge_base_file_part],
                    ttl=datetime.timedelta(hours=6),
                )
                
                agent.cache_id = cached_content.name
                agent.save()
                logger.info(f"Successfully created cache: {agent.cache_id}")

            except FileNotFoundError:
                return JsonResponse({"error": "Knowledge base directory not found."}, status=400)
            except Exception as e:
                logger.exception(f"Failed to create cache: {e}")
                return JsonResponse({"error": f"Failed to create cache: {str(e)}"}, status=500)

        model = GenerativeModel.from_cached_content(cached_content=cached_content)
        
    except Exception as e:
        return JsonResponse({"error": f"An error occurred during model setup: {str(e)}"}, status=500)

    # Build conversation history
    history = []
    chat_history = ChatHistory.objects.filter(agent=agent).first()

    if chat_history:
        chat_history_messages = chat_history.messages.all().order_by('created_at')
        for message in chat_history_messages:
            history.append(Content(role="user", parts=[Part.from_text(message.user_message)]))
            history.append(Content(role="model", parts=[Part.from_text(message.bot_message)]))
    else:
        chat_history_title = f"{request.user.username}_{agent_name}_history"
        chat_history = ChatHistory.objects.create(agent=agent, title=chat_history_title)

    chat = model.start_chat(history=history)

    if request.method == "POST":
        user_message = request.POST.get('message')
        if not user_message:
            return JsonResponse({"error": "No message provided"}, status=400)

        response = chat.send_message(user_message, stream=False)
        chatbot_response = response.text

        # Save message to chat history
        Message.objects.create(
            history=chat_history,
            user_message=user_message,
            bot_message=chatbot_response
        )

        return JsonResponse({"response": chatbot_response})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
