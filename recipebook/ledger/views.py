from django.shortcuts import render
from ledger.models import Ingredient, Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User

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

    author = User.objects.first()
    if not author:
        raise Exception("No user found to assign as author. Create a superuser first!")

    for recipe_info in recipe_data['recipes']:
        recipe, _ = Recipe.objects.get_or_create(name=recipe_info['name'], defaults={"author": author})
        recipe.author = author 
        recipe.save()

        for ingredient_info in recipe_info['ingredients']:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_info['name'])

            RecipeIngredient.objects.get_or_create(
                quantity=ingredient_info['quantity'],
                ingredient=ingredient,
                recipe=recipe
            )

    for recipe_info in recipe_data['recipes']:
        recipe, _ = Recipe.objects.get_or_create(name=recipe_info['name'])

        for ingredient_info in recipe_info['ingredients']:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_info['name'])

            RecipeIngredient.objects.create(
                quantity=ingredient_info['quantity'],
                ingredient=ingredient,
                recipe=recipe
            )

def index(request):
    load_recipes() 
    return render(request, 'ledger/index.html')

@login_required
def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('ledger:recipe_list')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'ledger/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('ledger:login')

def custom_login_view(request):
    if request.user.is_authenticated:
        return redirect('ledger:recipe_list')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('ledger:recipe_list')
    else:
        form = AuthenticationForm()

    return render(request, 'ledger/login.html', {'form': form})


def custom_logout_view(request):
    logout(request)
    return redirect('ledger:login')