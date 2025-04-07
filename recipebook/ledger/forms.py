from django import forms
from .models import Recipe, RecipeImage, RecipeIngredient, Ingredient
from django.forms import modelformset_factory

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'image']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']

RecipeIngredientFormSet = modelformset_factory(
    RecipeIngredient,
    form=RecipeIngredientForm,
    extra=1,
    can_delete=False
)