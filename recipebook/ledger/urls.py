from django.urls import path
from . import views

app_name = "ledger"

urlpatterns = [
    path('', views.index, name="index"),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/list', views.recipe_list, name="recipe_list"),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('ingredient/add/', views.ingredient_add_view, name='ingredient_add'),
    path('recipe/add/', views.recipe_add_view, name='recipe_add'),
    path('recipe/<int:recipe_id>/add_image/', views.add_recipe_image_view, name='add_recipe_image'),
]
