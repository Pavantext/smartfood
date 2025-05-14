# SmartFood - AI-Powered Food Recommendation System

SmartFood is an intelligent food recommendation system that uses AI to suggest personalized food items based on your mood, meal time, and cravings. The system combines the power of Google's Gemini AI with semantic search to provide accurate and contextually relevant food recommendations.

## Features

- 🤖 AI-powered food recommendations using Google's Gemini AI
- 🍽️ Diverse food categories including:
  - South Indian cuisine
  - North Indian cuisine
  - Chinese cuisine
  - Fast Food
  - Drinks and Beverages
  - Snacks
- 🎯 Smart matching based on:
  - Mood
  - Meal time
  - Food preferences
  - Ingredients
- 🔍 Semantic search using sentence transformers
- 🏷️ Detailed food information including:
  - Ingredients
  - Region
  - Meal time
  - Mood tags

## Tech Stack

- Python 3.x
- Django
- Google Gemini AI
- Sentence Transformers
- scikit-learn
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smartfood.git
cd smartfood
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Populate the database with food items:
```bash
python manage.py populate_food_items
```

7. Start the development server:
```bash
python manage.py runserver
```

## Usage

1. Open your web browser and navigate to `http://localhost:8000`
2. Enter your current mood, meal time, or food craving in the input field
3. The system will analyze your input and recommend the most suitable food items
4. Get detailed information about the recommended food, including ingredients and mood tags

## Example Inputs

- "I'm feeling happy and want something spicy for lunch"
- "Need something light and healthy for breakfast"
- "Craving something sweet and refreshing"
- "Want comfort food for dinner"
- "Looking for a quick snack"

## Project Structure

```
smartfood/
├── recommender/
│   ├── management/
│   │   └── commands/
│   │       └── populate_food_items.py
│   │   
│   ├── models.py
│   ├── utils.py
│   └── views.py
├── smartfood/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env
├── manage.py
└── requirements.txt
```

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature/your-feature-name`
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini AI for providing the AI capabilities
- Sentence Transformers for semantic search functionality
- Django framework for the web application structure

## Contact

For any questions or suggestions, please open an issue in the GitHub repository. 