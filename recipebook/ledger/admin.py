from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Profile)
