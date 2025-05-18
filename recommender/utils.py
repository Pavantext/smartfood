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
        gemini = genai.GenerativeModel(model_name="tunedModels/south-indian-food-bot-8901")
        prompt = f"""
You are a smart, friendly, and highly intuitive food assistant designed to give personalized dish recommendations.

You will be provided with:
1. A list of available food items in JSON format.
2. The user's input, which may include preferences, mood, cravings, time of day, or even weather conditions.

Each food item includes:
- Name
- Ingredients
- Region
- Meal time (e.g., Breakfast, Lunch, Dinner, Starter)
- Mood tags (e.g., comforting, spicy, refreshing)
- Description

### Your task:
Analyze the user's input carefully and match it to **one** most appropriate food item from the list.

Consider the following when making a recommendation:
- Current weather or temperature context (e.g., hot/cold day)
- Whether the user wants a drink or food
- The user's mood or emotional state (e.g., happy, tired, sad)
- Cravings or ingredient mentions (e.g., "I want something spicy")
- Time of day (e.g., lunch, dinner, snack)
- Regional preference if mentioned

### Output Format:
Respond in the following format:
1. **Food Name**: <name>
2. **Reason**: Explain why this food is the best match based on user input and food details.
3. **Suggestion**: A friendly and engaging sentence suggesting the dish (as if you're talking to the user directly).

### Available Food Items:
{food_list_str}

### User Input:
"{user_input}"

Your response:
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
