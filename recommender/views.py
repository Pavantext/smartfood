from django.shortcuts import render
from .models import FoodItem
from .utils import get_recommendation  # we'll build this
import os

def index(request):
    response = ""
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        response = get_recommendation(user_input)
    return render(request, "recommender/index.html", {"response": response})
