from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.

def load_recipes():
    with open('ledger/data/recipes.json', 'r') as f:
        return json.load(f)["recipes"]
    
def index(request):
    return render(request, 'ledger/index.html')

def recipe_detail(request, id):
    recipes = load_recipes()
    recipe = recipes[id - 1]
    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe})

def recipe_list(request):
    recipes = load_recipes()
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})