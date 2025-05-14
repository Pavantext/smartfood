from django.core.management.base import BaseCommand
from recommender.models import FoodItem

class Command(BaseCommand):
    help = 'Populates the database with diverse food items'

    def handle(self, *args, **kwargs):
        food_items = [
            # South Indian
            {
                'name': 'Masala Dosa',
                'ingredients': 'Rice batter, potatoes, onions, spices, ghee',
                'region': 'South Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'comfort, traditional, filling, energizing'
            },
            {
                'name': 'Idli Sambar',
                'ingredients': 'Rice, urad dal, sambar, coconut chutney',
                'region': 'South Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'light, healthy, traditional, comforting'
            },
            {
                'name': 'Hyderabadi Biryani',
                'ingredients': 'Basmati rice, chicken, spices, saffron, mint',
                'region': 'South Indian',
                'meal_time': 'Lunch',
                'mood_tags': 'rich, aromatic, celebratory, indulgent'
            },

            # North Indian
            {
                'name': 'Butter Chicken',
                'ingredients': 'Chicken, tomatoes, butter, cream, spices',
                'region': 'North Indian',
                'meal_time': 'Dinner',
                'mood_tags': 'rich, creamy, indulgent, comforting'
            },
            {
                'name': 'Chole Bhature',
                'ingredients': 'Chickpeas, flour, spices, onions, tomatoes',
                'region': 'North Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'filling, spicy, traditional, energizing'
            },
            {
                'name': 'Rogan Josh',
                'ingredients': 'Lamb, yogurt, spices, onions, tomatoes',
                'region': 'North Indian',
                'meal_time': 'Dinner',
                'mood_tags': 'rich, aromatic, indulgent, warming'
            },

            # Chinese
            {
                'name': 'Veg Noodles',
                'ingredients': 'Noodles, mixed vegetables, soy sauce, garlic',
                'region': 'Chinese',
                'meal_time': 'Lunch',
                'mood_tags': 'quick, light, healthy, energizing'
            },
            {
                'name': 'Manchurian',
                'ingredients': 'Cauliflower, soy sauce, garlic, ginger',
                'region': 'Chinese',
                'meal_time': 'Dinner',
                'mood_tags': 'spicy, flavorful, indulgent, exciting'
            },
            {
                'name': 'Dim Sum',
                'ingredients': 'Flour, vegetables, meat, soy sauce',
                'region': 'Chinese',
                'meal_time': 'Lunch',
                'mood_tags': 'delicate, social, light, fun'
            },

            # Fast Food
            {
                'name': 'Veg Burger',
                'ingredients': 'Bun, vegetable patty, lettuce, cheese, sauce',
                'region': 'Fast Food',
                'meal_time': 'Lunch',
                'mood_tags': 'quick, convenient, satisfying, casual'
            },
            {
                'name': 'Pizza Margherita',
                'ingredients': 'Dough, tomato sauce, mozzarella, basil',
                'region': 'Fast Food',
                'meal_time': 'Dinner',
                'mood_tags': 'comforting, social, casual, indulgent'
            },
            {
                'name': 'French Fries',
                'ingredients': 'Potatoes, salt, oil',
                'region': 'Fast Food',
                'meal_time': 'Snack',
                'mood_tags': 'crispy, salty, indulgent, casual'
            },

            # Drinks and Beverages
            {
                'name': 'Masala Chai',
                'ingredients': 'Tea leaves, milk, spices, sugar',
                'region': 'Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'warming, comforting, energizing, traditional'
            },
            {
                'name': 'Lassi',
                'ingredients': 'Yogurt, sugar, cardamom, rose water',
                'region': 'Indian',
                'meal_time': 'Any',
                'mood_tags': 'refreshing, cooling, sweet, traditional'
            },
            {
                'name': 'Fresh Lime Soda',
                'ingredients': 'Lime, soda, salt, sugar',
                'region': 'Indian',
                'meal_time': 'Any',
                'mood_tags': 'refreshing, cooling, energizing, light'
            },

            # Snacks
            {
                'name': 'Samosa',
                'ingredients': 'Flour, potatoes, peas, spices',
                'region': 'Indian',
                'meal_time': 'Snack',
                'mood_tags': 'crispy, spicy, satisfying, traditional'
            },
            {
                'name': 'Bhel Puri',
                'ingredients': 'Puffed rice, vegetables, chutney, sev',
                'region': 'Indian',
                'meal_time': 'Snack',
                'mood_tags': 'crunchy, tangy, refreshing, fun'
            },
            {
                'name': 'Pav Bhaji',
                'ingredients': 'Mixed vegetables, butter, pav, spices',
                'region': 'Indian',
                'meal_time': 'Snack',
                'mood_tags': 'spicy, filling, comforting, street food'
            }
        ]

        # Clear existing food items
        FoodItem.objects.all().delete()

        # Create new food items
        for item in food_items:
            FoodItem.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Successfully populated food items')) 