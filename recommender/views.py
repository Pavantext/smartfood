from django.shortcuts import render
from django.http import JsonResponse
from .models import FoodItem, Conversation, Message
from .utils import get_recommendation
import uuid
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

def get_or_create_conversation(request):
    session_id = request.session.get('conversation_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session['conversation_id'] = session_id
    
    conversation, created = Conversation.objects.get_or_create(session_id=session_id)
    return conversation

def index(request):
    conversation = get_or_create_conversation(request)
    messages = conversation.messages.all()
    return render(request, "recommender/index.html", {
        "messages": messages,
        "conversation_id": conversation.session_id
    })

@csrf_exempt
def clear_session(request):
    if request.method == 'POST':
        # Clear the session
        if 'conversation_id' in request.session:
            # Delete all messages for the current conversation
            conversation = get_or_create_conversation(request)
            conversation.messages.all().delete()
            
            # Generate a new session ID
            new_session_id = str(uuid.uuid4())
            request.session['conversation_id'] = new_session_id
            
            # Create a new conversation
            Conversation.objects.create(session_id=new_session_id)
            
            return JsonResponse({'status': 'success'})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('message')
        conversation = get_or_create_conversation(request)
        
        # Save user message
        Message.objects.create(
            conversation=conversation,
            content=user_input,
            is_user=True
        )
        
        # Get AI response
        response = get_recommendation(user_input, conversation)
        
        # Save AI response
        Message.objects.create(
            conversation=conversation,
            content=response,
            is_user=False
        )
        
        return JsonResponse({
            'response': response,
            'timestamp': timezone.now().isoformat()
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
