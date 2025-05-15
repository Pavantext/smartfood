from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from .models import FoodItem, Message
from django.conf import settings
import google.generativeai as genai
import numpy as np
import os

# Debug: Print API key status (remove in production)
api_key = settings.GEMINI_API_KEY
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")

genai.configure(api_key=api_key)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_conversation_context(conversation, limit=5):
    """Get recent conversation history for context"""
    recent_messages = Message.objects.filter(
        conversation=conversation
    ).order_by('-timestamp')[:limit]
    
    context = []
    for msg in reversed(recent_messages):
        role = "User" if msg.is_user else "Assistant"
        context.append(f"{role}: {msg.content}")
    
    return "\n".join(context)

def get_recommendation(user_input, conversation=None):
    try:
        # Get conversation context
        context = ""
        if conversation:
            context = get_conversation_context(conversation)
            context = f"Previous conversation:\n{context}\n\n"

        # Step 1: Let Gemini analyze the input with context
        gemini = genai.GenerativeModel("gemini-2.0-flash")
        food_items = FoodItem.objects.all()
        food_list = ""
        for idx, food in enumerate(food_items, 1):
            food_list += f"{idx}. {food.name}: {food.ingredients}. {food.description if hasattr(food, 'description') else ''}\n"

        prompt = f"""
        You are an expert food recommender. Here is a list of food and drink items:

        {food_list}

        The user says: "{user_input}"

        Based on the food and drink names and descriptions, recommend the most suitable item for the user. Consider the weather, the user's desire for a warm drink, and any other relevant context. Explain your choice in a friendly, conversational way.
        """

        ai_info = gemini.generate_content(prompt).text

        # Step 2: Find best food matches
        query = user_input
        query_vector = embedding_model.encode(query)

        all_foods = FoodItem.objects.all()
        food_vectors = []
        food_names = []

        for food in all_foods:
            description = f"{food.name} with {food.ingredients} for {food.meal_time} - {food.mood_tags}"
            food_vectors.append(embedding_model.encode(description))
            food_names.append(food.name)

        if not food_vectors:
            return "I'm still learning about different foods. Could you tell me more about what you're looking for?"

        scores = cosine_similarity([query_vector], food_vectors)[0]
        best_index = int(np.argmax(scores))
        best_food = all_foods[best_index]

        # Step 3: Generate a conversational response
        response_prompt = f"""
        Context: {context}
        User's current input: {user_input}
        Analysis: {ai_info}
        Recommended food: {best_food.name}
        
        Generate a friendly, conversational response that:
        1. Acknowledges the user's input
        2. Mentions the recommended food naturally
        3. Includes some details about the food
        4. Asks a follow-up question to keep the conversation going
        """

        response = gemini.generate_content(response_prompt).text
        return response

    except Exception as e:
        return f"I'm having trouble understanding right now. Could you rephrase that? (Error: {str(e)})"
