from django.shortcuts import render
from ledger.models import Ingredient, Recipe, RecipeIngredient

def load_recipes():
    recipe_data = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {"name": "tomato", "quantity": "3pcs"},
                    {"name": "onion", "quantity": "1pc"},
                    {"name": "pork", "quantity": "1kg"},
                    {"name": "water", "quantity": "1L"},
                    {"name": "sinigang mix", "quantity": "1 packet"}
                ]
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {"name": "garlic", "quantity": "1 head"},
                    {"name": "onion", "quantity": "1pc"},
                    {"name": "vinegar", "quantity": "1/2cup"},
                    {"name": "water", "quantity": "1 cup"},
                    {"name": "salt", "quantity": "1 tablespoon"},
                    {"name": "whole black peppers", "quantity": "1 tablespoon"},
                    {"name": "pork", "quantity": "1 kilo"}
                ]
            }
        ]
    }

    for recipe_info in recipe_data['recipes']:
        recipe, _ = Recipe.objects.get_or_create(name=recipe_info['name'])[0]

        for ingredient_info in recipe_info['ingredients']:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_info['name'])[0]

            RecipeIngredient.objects.create(
                quantity=ingredient_info['quantity'],
                ingredient=ingredient,
                recipe=recipe
            )

def index(request):
    load_recipes() 
    return render(request, 'ledger/index.html')

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})