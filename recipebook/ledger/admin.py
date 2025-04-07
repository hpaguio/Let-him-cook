from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Recipe, RecipeImage, Ingredient, RecipeIngredient, Profile

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInline]

admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(Profile)