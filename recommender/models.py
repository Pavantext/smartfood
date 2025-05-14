from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    region = models.CharField(max_length=50)
    meal_time = models.CharField(max_length=50)
    mood_tags = models.CharField(max_length=255)  # comma-separated

    def __str__(self):
        return self.name
