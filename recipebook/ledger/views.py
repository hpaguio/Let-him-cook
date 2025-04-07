from django.shortcuts import render, redirect, get_object_or_404
from ledger.models import Ingredient, Recipe, RecipeIngredient
from .forms import RecipeForm, IngredientForm, RecipeImageForm, RecipeIngredientForm, RecipeIngredientFormSet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Ingredient, RecipeIngredient
from django.forms import modelformset_factory

IngredientFormSet = modelformset_factory(
    RecipeIngredient,
    fields=('ingredient', 'quantity'),
    extra=1,
    can_delete=False
)

def index(request):
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

@login_required
def recipe_add_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        formset = IngredientFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            ingredients = formset.save(commit=False)
            for ingredient in ingredients:
                ingredient.recipe = recipe
                ingredient.save()
            
            formset.save_m2m()

            return redirect('ledger:recipe_detail', id=recipe.id)
    else:
        form = RecipeForm()
        formset = IngredientFormSet()
    return render(request, 'ledger/recipe_add.html', {'form': form, 'formset': formset})


@login_required
def add_recipe_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect('recipe_detail', id=pk)
    else:
        form = RecipeImageForm()

    return render(request, 'ledger/recipe_image_add.html', {'form': form, 'recipe': recipe})

@login_required
def ingredient_add_view(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ledger:recipe_add')
    else:
        form = IngredientForm()
    return render(request, 'ledger/ingredient_add.html', {'form': form})

@login_required
def add_recipe_image_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('ledger:recipe_detail', id=recipe.id)
    else:
        form = RecipeImageForm()

    return render(request, 'ledger/add_recipe_image.html', {
        'form': form,
        'recipe': recipe
    })
