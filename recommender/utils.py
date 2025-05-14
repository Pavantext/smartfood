from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from .models import FoodItem
import google.generativeai as genai
import numpy as np
from django.conf import settings
import os

# Debug: Print API key status (remove in production)
api_key = settings.GEMINI_API_KEY
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")

genai.configure(api_key=api_key)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_recommendation(user_input):
    try:
        # Debug: Check database state
        all_foods = FoodItem.objects.all()
        print(f"Number of food items in database: {all_foods.count()}")
        
        if all_foods.count() == 0:
            # Try to populate the database if empty
            from django.core.management import call_command
            call_command('populate_food_items')
            all_foods = FoodItem.objects.all()
            print(f"After population - Number of food items: {all_foods.count()}")

        # Step 1: Let Gemini extract mood, meal_time, craving
        gemini = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"Extract mood, meal time, and food craving from: '{user_input}'"
        ai_info = gemini.generate_content(prompt).text

        # (Optional) parse AI info using regex or simple logic
        query = user_input  # or refine it using ai_info
        query_vector = embedding_model.encode(query)

        # Step 2: Find best food matches
        food_vectors = []
        food_names = []

        for food in all_foods:
            description = f"{food.name} with {food.ingredients} for {food.meal_time} - {food.mood_tags}"
            food_vectors.append(embedding_model.encode(description))
            food_names.append(food.name)

        if not food_vectors:
            return "Sorry, no food items in the database yet. Please run 'python manage.py populate_food_items' to populate the database."

        scores = cosine_similarity([query_vector], food_vectors)[0]
        best_index = int(np.argmax(scores))  # Convert numpy.int64 to Python int
        best_food = all_foods[best_index]

        # Step 3: Let Gemini generate a nice response
        response = gemini.generate_content(
            f"User is feeling: {ai_info}. Recommend the food: {best_food.name} in a friendly tone."
        ).text

        return response
    except Exception as e:
        return f"Error: {str(e)}"
