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
                'mood_tags': 'comfort, traditional, filling, energizing',
                'description': 'A crispy, savory crepe made from a fermented rice batter, filled with a mix of potatoes, onions, and spices. Served with a side of chutney, it is a popular breakfast or snack.'
            },
            {
                'name': 'Idli Sambar',
                'ingredients': 'Rice, urad dal, sambar, coconut chutney',
                'region': 'South Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'light, healthy, traditional, comforting',
                'description': 'Soft, steamed rice cakes served with a tangy, spicy sambar sauce and coconut chutney. A popular breakfast or snack in South India.'
            },
            {
                'name': 'Hyderabadi Biryani',
                'ingredients': 'Basmati rice, chicken, spices, saffron, mint',
                'region': 'South Indian',
                'meal_time': 'Lunch',
                'mood_tags': 'rich, aromatic, celebratory, indulgent',
                'description': 'A fragrant rice dish cooked with a blend of spices, saffron, and mint. Served with a generous amount of chicken, it is a popular dish for special occasions and celebrations.'
            },
            {
                'name': 'Medu Vada',
                'ingredients': 'Urad dal, spices, curry leaves, oil',
                'region': 'South Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'crispy, savory, traditional, energizing',
                'description': 'A savory, deep-fried doughnut-shaped snack made from urad dal batter, crispy on the outside and soft inside. Often served with coconut chutney and sambar, popular for breakfast or as a snack.'
            },
            {
                'name': 'Pongal',
                'ingredients': 'Rice, moong dal, ghee, black pepper, cashews',
                'region': 'South Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'comforting, mild, traditional, filling',
                'description': 'A creamy, mildly spiced rice and lentil dish cooked with ghee, black pepper, and cashews. Served hot, it is a comforting breakfast especially during festivals or winter.'
            },
            {
                'name': 'Sambar Rice',
                'ingredients': 'Rice, toor dal, vegetables, sambar powder, tamarind',
                'region': 'South Indian',
                'meal_time': 'Lunch',
                'mood_tags': 'comforting, wholesome, traditional, filling',
                'description': 'A classic combination of steamed rice mixed with flavorful sambar, made with lentils, vegetables, and aromatic spices. A complete meal that embodies South Indian home cooking.'
            },
            {
                'name': 'Rasam',
                'ingredients': 'Tamarind, tomatoes, lentils, rasam powder, curry leaves',
                'region': 'South Indian',
                'meal_time': 'Dinner',
                'mood_tags': 'light, soothing, digestive, warming',
                'description': 'A tangy and aromatic soup made with tamarind, tomatoes, and spices. Often served with rice or consumed as a digestive drink, perfect for cold evenings or when feeling under the weather.'
            },
            {
                'name': 'Upma',
                'ingredients': 'Semolina, vegetables, mustard seeds, curry leaves',
                'region': 'South Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'light, healthy, quick, comforting',
                'description': 'A savory porridge made from roasted semolina, tempered with mustard seeds and curry leaves. Often packed with vegetables, it is a popular quick breakfast option.'
            },
            {
                'name': 'Uttapam',
                'ingredients': 'Fermented rice batter, onions, tomatoes, green chilies',
                'region': 'South Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'soft, savory, fermented, healthy',
                'description': 'A thick pancake made from fermented rice batter, topped with vegetables. Softer than dosa with a slight tanginess from fermentation, often served with chutney.'
            },
            {
                'name': 'Avial',
                'ingredients': 'Mixed vegetables, coconut, yogurt, curry leaves',
                'region': 'South Indian',
                'meal_time': 'Lunch',
                'mood_tags': 'nutritious, traditional, festival, coconutty',
                'description': 'A thick vegetable curry made with coconut paste and yogurt, seasoned with coconut oil. A staple in Kerala sadhya (festive meals), celebrating local produce.'
            },
            {
                'name': 'Kerala Fish Curry',
                'ingredients': 'Fish, coconut milk, kokum, shallots, spices',
                'region': 'South Indian',
                'meal_time': 'Dinner',
                'mood_tags': 'tangy, coconut-based, coastal, aromatic',
                'description': 'A signature Malabar coast dish where fish is simmered in a coconut milk gravy with kokum and spices. Best enjoyed with steamed red rice or appam.'
            },
            {
                'name': 'Bisibele Bath',
                'ingredients': 'Rice, lentils, vegetables, bisibele bath powder, ghee',
                'region': 'South Indian',
                'meal_time': 'Lunch',
                'mood_tags': 'spicy, flavorful, one-pot-meal, festival',
                'description': 'A hearty Karnataka specialty combining rice, lentils, and vegetables in a spicy masala paste. Traditionally served with potato chips and boondi.'
            },
            {
                'name': 'Appam with Stew',
                'ingredients': 'Fermented rice batter, coconut milk, vegetables, coconut oil',
                'region': 'South Indian',
                'meal_time': 'Dinner',
                'mood_tags': 'soft, lacy, coconutty, comforting',
                'description': 'Lacy rice hoppers with crispy edges and soft center, paired with a mild vegetable or chicken stew in coconut milk. A Kerala favorite for Sunday breakfasts.'
            },

            # North Indian
            {
                'name': 'Butter Chicken',
                'ingredients': 'Chicken, tomatoes, butter, cream, spices',
                'region': 'North Indian',
                'meal_time': 'Dinner',
                'mood_tags': 'rich, creamy, indulgent, comforting',
                'description': 'A creamy, rich chicken curry with a smooth, creamy texture, made with tomatoes, butter, and cream. A popular dish for special occasions and celebrations.'
            },
            {
                'name': 'Chole Bhature',
                'ingredients': 'Chickpeas, flour, spices, onions, tomatoes',
                'region': 'North Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'filling, spicy, traditional, energizing',
                'description': 'A spicy, filling dish of chickpeas cooked with a blend of spices, served with a soft, fluffy bread called bhatura. A popular breakfast or snack in North India.'
            },
            {
                'name': 'Rogan Josh',
                'ingredients': 'Lamb, yogurt, spices, onions, tomatoes',
                'region': 'North Indian',
                'meal_time': 'Dinner',
                'mood_tags': 'rich, aromatic, indulgent, warming',
                'description': 'A rich, aromatic lamb curry with a smooth, creamy texture, made with yogurt, spices, onions, and tomatoes. A popular dish for special occasions and celebrations.'
            },
            {
                'name': 'Rajma Chawal',
                'ingredients': 'Kidney beans, rice, tomatoes, spices',
                'region': 'North Indian',
                'meal_time': 'Lunch',
                'mood_tags': 'hearty, comforting, homely, filling',
                'description': 'A classic North Indian comfort food of red kidney beans cooked in a spiced tomato gravy, served with steamed rice. Popular as a wholesome lunch or dinner.'
            },
            {
                'name': 'Paneer Butter Masala',
                'ingredients': 'Paneer, tomatoes, cream, butter, spices',
                'region': 'North Indian',
                'meal_time': 'Dinner',
                'mood_tags': 'rich, creamy, indulgent, festive',
                'description': 'Soft paneer cubes simmered in a rich, creamy tomato and butter gravy. A favorite vegetarian dish for special occasions and festive dinners.'
            },

            # Chinese
            {
                'name': 'Veg Noodles',
                'ingredients': 'Noodles, mixed vegetables, soy sauce, garlic',
                'region': 'Chinese',
                'meal_time': 'Lunch',
                'mood_tags': 'quick, light, healthy, energizing',
                'description': 'A quick and light dish of stir-fried noodles with mixed vegetables, soy sauce, and garlic. A popular choice for a quick lunch or snack.'
            },
            {
                'name': 'Manchurian',
                'ingredients': 'Cauliflower, soy sauce, garlic, ginger',
                'region': 'Chinese',
                'meal_time': 'Dinner',
                'mood_tags': 'spicy, flavorful, indulgent, exciting',
                'description': 'A spicy and flavorful dish of cauliflower florets coated in a thick, tangy sauce made with soy sauce, garlic, and ginger. A popular choice for a hearty dinner or snack.'
            },
            {
                'name': 'Dim Sum',
                'ingredients': 'Flour, vegetables, meat, soy sauce',
                'region': 'Chinese',
                'meal_time': 'Lunch',
                'mood_tags': 'delicate, social, light, fun',
                'description': 'Delicate, bite-sized steamed dumplings filled with a mix of vegetables, meat, and soy sauce. A popular choice for a social lunch or snack.'
            },
            {
                'name': 'Spring Rolls',
                'ingredients': 'Flour wrappers, mixed vegetables, soy sauce, oil',
                'region': 'Chinese',
                'meal_time': 'Snack',
                'mood_tags': 'crispy, light, fun, party',
                'description': 'Crispy rolls filled with stir-fried vegetables, wrapped in thin flour sheets and deep-fried. Served with sweet chili sauce, they are a popular party snack.'
            },
            {
                'name': 'Hot and Sour Soup',
                'ingredients': 'Mushrooms, tofu, bamboo shoots, vinegar, pepper',
                'region': 'Chinese',
                'meal_time': 'Starter',
                'mood_tags': 'spicy, tangy, warming, appetizing',
                'description': 'A spicy and tangy soup made with mushrooms, tofu, bamboo shoots, and seasoned with vinegar and pepper. Served hot, it is a favorite starter in Chinese cuisine.'
            },

            # Fast Food
            {
                'name': 'Veg Burger',
                'ingredients': 'Bun, vegetable patty, lettuce, cheese, sauce',
                'region': 'Fast Food',
                'meal_time': 'Lunch',
                'mood_tags': 'quick, convenient, satisfying, casual',
                'description': 'A quick and convenient burger made with a vegetable patty, lettuce, cheese, and a sauce. A popular choice for a quick lunch or snack.'
            },
            {
                'name': 'Pizza Margherita',
                'ingredients': 'Dough, tomato sauce, mozzarella, basil',
                'region': 'Fast Food',
                'meal_time': 'Dinner',
                'mood_tags': 'comforting, social, casual, indulgent',
                'description': 'A classic pizza with a thin crust, tomato sauce, mozzarella cheese, and basil. A popular choice for a comforting dinner or snack.'
            },
            {
                'name': 'French Fries',
                'ingredients': 'Potatoes, salt, oil',
                'region': 'Fast Food',
                'meal_time': 'Snack',
                'mood_tags': 'crispy, salty, indulgent, casual',
                'description': 'Crispy, golden-brown French fries, seasoned with salt and served with a side of ketchup. A popular snack for kids and adults alike.'
            },
            {
                'name': 'Chicken Nuggets',
                'ingredients': 'Chicken, breadcrumbs, spices, oil',
                'region': 'Fast Food',
                'meal_time': 'Snack',
                'mood_tags': 'crispy, savory, quick, kid-friendly',
                'description': 'Bite-sized pieces of chicken coated in breadcrumbs and deep-fried until golden and crispy. A popular snack for kids and adults alike.'
            },
            {
                'name': 'Grilled Sandwich',
                'ingredients': 'Bread, cheese, vegetables, butter',
                'region': 'Fast Food',
                'meal_time': 'Breakfast',
                'mood_tags': 'quick, cheesy, satisfying, casual',
                'description': 'A hot sandwich made with bread, cheese, and assorted vegetables, grilled to perfection. A quick and satisfying breakfast or snack.'
            },

            # Drinks and Beverages
            {
                'name': 'Masala Chai',
                'ingredients': 'Tea leaves, milk, spices, sugar',
                'region': 'Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'warming, comforting, energizing, traditional',
                'description': 'A hot, spiced Indian tea made with black tea leaves, milk, and a blend of warming spices like ginger, cardamom, and cinnamon. Perfect for cold or rainy days.'
            },
            {
                'name': 'Hot Chocolate',
                'ingredients': 'Cocoa, milk, sugar',
                'region': 'Western',
                'meal_time': 'Any',
                'mood_tags': 'warm, comforting, sweet, cozy',
                'description': 'A rich, creamy beverage made by mixing cocoa powder and sugar with hot milk. Often enjoyed during winter or rainy weather for its comforting warmth.'
            },
            {
                'name': 'Ginger Tea',
                'ingredients': 'Ginger, tea leaves, water, honey',
                'region': 'Indian',
                'meal_time': 'Any',
                'mood_tags': 'warming, soothing, healthy',
                'description': 'A herbal tea made by boiling fresh ginger with tea leaves and sweetened with honey. Known for its soothing effect on the throat and warming properties, especially on cold or rainy days.'
            },
            {
                'name': 'Tomato Soup',
                'ingredients': 'Tomatoes, cream, spices, herbs',
                'region': 'Global',
                'meal_time': 'Snack',
                'mood_tags': 'warm, comforting, light',
                'description': 'A smooth, creamy soup made from ripe tomatoes and seasoned with herbs. Served hot, it is a popular comfort food during rainy or chilly weather.'
            },
            {
                'name': 'Sweet Corn Soup',
                'ingredients': 'Sweet corn, vegetables, broth, spices',
                'region': 'Indo-Chinese',
                'meal_time': 'Snack',
                'mood_tags': 'warm, light, healthy',
                'description': 'A light and mildly sweet soup made with sweet corn and mixed vegetables. Served hot, it is a favorite starter during monsoon and winter.'
            },
            {
                'name': 'Filter Coffee',
                'ingredients': 'Coffee powder, milk, sugar, water',
                'region': 'South Indian',
                'meal_time': 'Breakfast',
                'mood_tags': 'energizing, traditional, warm',
                'description': 'A strong, aromatic coffee made by percolating ground coffee beans and served with hot milk. A staple in South Indian households, especially enjoyed in the morning or on rainy days.'
            },
            {
                'name': 'Lassi',
                'ingredients': 'Yogurt, sugar, cardamom, rose water',
                'region': 'Indian',
                'meal_time': 'Any',
                'mood_tags': 'refreshing, cooling, sweet, traditional',
                'description': 'A chilled yogurt-based drink, sweetened and flavored with cardamom or rose water. Popular in summer for its cooling effect.'
            },
            {
                'name': 'Fresh Lime Soda',
                'ingredients': 'Lime, soda, salt, sugar',
                'region': 'Indian',
                'meal_time': 'Any',
                'mood_tags': 'refreshing, cooling, energizing, light',
                'description': 'A tangy and refreshing cold drink made with fresh lime juice, soda, and a mix of salt and sugar. Perfect for hot days.'
            },
            {
                'name': 'Pumpkin Soup',
                'ingredients': 'Pumpkin, cream, spices, herbs',
                'region': 'Global',
                'meal_time': 'Dinner',
                'mood_tags': 'warm, creamy, comforting',
                'description': 'A velvety soup made from pureed pumpkin, cream, and warming spices. Served hot, it is a comforting dish for cold evenings.'
            },
            {
                'name': 'Turmeric Milk',
                'ingredients': 'Milk, turmeric, black pepper, honey',
                'region': 'Indian',
                'meal_time': 'Night',
                'mood_tags': 'soothing, healthy, warm',
                'description': 'A traditional Indian drink made by mixing turmeric and black pepper into hot milk, often sweetened with honey. Known for its health benefits and soothing properties, especially before bedtime or during illness.'
            },
            {
                'name': 'Green Tea',
                'ingredients': 'Green tea leaves, water',
                'region': 'Asian',
                'meal_time': 'Any',
                'mood_tags': 'light, healthy, refreshing',
                'description': 'A light, antioxidant-rich tea made from green tea leaves. Usually served hot and enjoyed for its health benefits and subtle flavor.'
            },
            {
                'name': 'Buttermilk (Chaas)',
                'ingredients': 'Yogurt, water, cumin, salt, herbs',
                'region': 'Indian',
                'meal_time': 'Lunch',
                'mood_tags': 'cooling, light, digestive, refreshing',
                'description': 'A traditional Indian drink made by blending yogurt with water, salt, and spices like cumin. Served chilled, it aids digestion and is perfect for hot days.'
            },
            {
                'name': 'Espresso',
                'ingredients': 'Coffee beans, water',
                'region': 'Western',
                'meal_time': 'Any',
                'mood_tags': 'strong, energizing, bold',
                'description': 'A concentrated coffee beverage brewed by forcing hot water through finely-ground coffee beans. Known for its strong flavor and quick energy boost.'
            },

            # Snacks
            {
                'name': 'Samosa',
                'ingredients': 'Flour, potatoes, peas, spices',
                'region': 'Indian',
                'meal_time': 'Snack',
                'mood_tags': 'crispy, spicy, satisfying, traditional',
                'description': 'A crispy, triangular pastry filled with a mix of potatoes, peas, and spices. A popular snack for kids and adults alike.'
            },
            {
                'name': 'Bhel Puri',
                'ingredients': 'Puffed rice, vegetables, chutney, sev',
                'region': 'Indian',
                'meal_time': 'Snack',
                'mood_tags': 'crunchy, tangy, refreshing, fun',
                'description': 'A crunchy, tangy snack made with puffed rice, vegetables, chutney, and sev. A popular street food snack across India.'
            },
            {
                'name': 'Pav Bhaji',
                'ingredients': 'Mixed vegetables, butter, pav, spices',
                'region': 'Indian',
                'meal_time': 'Snack',
                'mood_tags': 'spicy, filling, comforting, street food',
                'description': 'A spicy, filling dish of mixed vegetables cooked in a rich, creamy sauce, served with a soft, fluffy bread called pav. A popular street food snack across India.'
            },
            {
                'name': 'Dhokla',
                'ingredients': 'Gram flour, yogurt, spices, fruit salt',
                'region': 'Indian',
                'meal_time': 'Snack',
                'mood_tags': 'light, spongy, tangy, healthy',
                'description': 'A steamed, spongy snack made from fermented gram flour batter, seasoned with mustard seeds and curry leaves. Served with green chutney, it is a popular Gujarati snack.'
            },
            {
                'name': 'Aloo Tikki',
                'ingredients': 'Potatoes, spices, breadcrumbs, oil',
                'region': 'Indian',
                'meal_time': 'Snack',
                'mood_tags': 'crispy, spicy, street food, filling',
                'description': 'Crispy potato patties spiced with Indian masalas, shallow-fried and served hot with chutneys. A favorite street food snack across India.'
            }
        ]

        # Clear existing food items
        FoodItem.objects.all().delete()

        # Create new food items
        for item in food_items:
            FoodItem.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Successfully populated food items')) 