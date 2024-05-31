# recipe/views.py

from django.shortcuts import render, get_object_or_404
from .models import Recipe
from datetime import datetime

def main(request):
    recipes = Recipe.objects.filter(date__year=2023)
    return render(request, 'recipe/main.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})
