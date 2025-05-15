from django.db import models
from django.utils import timezone

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    region = models.CharField(max_length=50)
    meal_time = models.CharField(max_length=50)
    mood_tags = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Conversation(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversation {self.session_id}"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    is_user = models.BooleanField(default=True)  # True for user messages, False for AI responses
    timestamp = models.DateTimeField(default=timezone.now)
    food_recommendation = models.ForeignKey(FoodItem, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{'User' if self.is_user else 'AI'}: {self.content[:50]}"
