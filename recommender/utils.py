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
        # 1. Load context if any
        context = get_conversation_context(conversation) if conversation else ""
        context_block = f"Previous conversation:\n{context}\n\n" if context else ""

        # 2. Get food items from DB
        food_items = list(FoodItem.objects.all())
        if not food_items:
            return "Oops! I don't have any food items yet. Please add some delicious dishes first."

        # 3. Compute embeddings for user input and food descriptions
        query_vector = embedding_model.encode(user_input)
        food_vectors = []
        for food in food_items:
            text = f"{food.name}, {food.ingredients}, {food.description}, {food.meal_time}, {food.mood_tags}"
            food_vectors.append(embedding_model.encode(text))
        food_vectors = np.array(food_vectors)

        # 4. Find the most relevant food item
        scores = cosine_similarity([query_vector], food_vectors)[0]
        best_index = int(np.argmax(scores))
        best_food = food_items[best_index]

        # 5. Friendly final response generation using Gemini
        gemini = genai.GenerativeModel(model_name="gemini-2.0-flash")

        final_prompt = f"""
You are a warm, smart, and cheerful food assistant.

You’ve already matched the best food item for the user from a curated database using semantic search.

Your task now is to explain **why** the chosen dish is a great fit for the user’s input and present it in a friendly, natural-sounding tone.

Be brief, joyful, and personal.

### Context (if any):
{context_block}

### User Input:
"{user_input}"

### Matched Food Item:
- **Name**: {best_food.name}
- **Ingredients**: {best_food.ingredients}
- **Meal Time**: {best_food.meal_time}
- **Mood Tags**: {best_food.mood_tags}
- **Description**: {best_food.description}

### Write a response that:
- Acknowledges the user's mood or craving.
- Explains why this food suits them.
- Mentions 1-2 interesting ingredients or features.
- Ends with a question or offer to suggest something else.

Response:
"""

        final_response = gemini.generate_content(final_prompt).text.strip()
        return final_response

    except Exception as e:
        return f"Sorry, something went wrong while thinking about that. Can you try rephrasing it? (Error: {str(e)})"



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
