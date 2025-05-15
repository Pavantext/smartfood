from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from .models import FoodItem, Message
from django.conf import settings
import google.generativeai as genai
import numpy as np
import os

# Configure Gemini API
api_key = settings.GEMINI_API_KEY
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")
genai.configure(api_key=api_key)

# Load embedding model
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
        # Context history
        context = get_conversation_context(conversation) if conversation else ""
        context_block = f"Previous conversation:\n{context}\n\n" if context else ""

        # Prepare food item descriptions
        food_items = list(FoodItem.objects.all())
        if not food_items:
            return "I don't have any food options yet to recommend. Please add some to the menu first."

        food_descriptions = []
        for idx, food in enumerate(food_items, 1):
            desc = (
                f"{idx}. {food.name} - Ingredients: {food.ingredients}. "
                f"Meal time: {food.meal_time}. Mood tags: {food.mood_tags}. "
                f"{food.description if hasattr(food, 'description') else ''}"
            )
            food_descriptions.append(desc)

        food_list_str = "\n".join(food_descriptions)

        # Gemini: Analyze the input and suggest the best food (semantic reasoning)
        gemini = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"""
        You are a smart and friendly food assistant.

        {context_block}
        Here is a list of available food items:
        {food_list_str}

        The user says: "{user_input}"

        Based on the available foods and user's input, recommend the single most suitable item.
        Consider:
        - Weather context (e.g., hot/cold)
        - Drink or food preference
        - Mood
        - Meal time (e.g., breakfast, lunch)
        - Ingredients or cravings

        Respond with:
        1. Food Name
        2. Reason for recommendation
        3. A friendly sentence to suggest it
        """

        gemini_response = gemini.generate_content(prompt).text.strip()

        # Embedding-based similarity search
        query_vector = embedding_model.encode(user_input)
        food_vectors = []
        for food in food_items:
            vector_text = f"{food.name}, {food.ingredients}, {food.description}, {food.meal_time}, {food.mood_tags}"
            food_vectors.append(embedding_model.encode(vector_text))
        food_vectors = np.array(food_vectors)

        scores = cosine_similarity([query_vector], food_vectors)[0]
        best_index = int(np.argmax(scores))
        best_food = food_items[best_index]

        # Final friendly response
        final_prompt = f"""
        {context_block}
        User's input: "{user_input}"
        Gemini's recommendation: {gemini_response}
        Best semantic match based on user input: {best_food.name} - {best_food.description}

        Write a single, friendly, natural-sounding response that:
        - Acknowledges the user's input
        - Explains the food choice clearly
        - Includes one or two ingredients or features
        - Asks a question or offers to suggest another item
        """

        final_response = gemini.generate_content(final_prompt).text.strip()
        return final_response

    except Exception as e:
        return f"I'm having trouble figuring that out right now. Could you rephrase? (Error: {str(e)})"
