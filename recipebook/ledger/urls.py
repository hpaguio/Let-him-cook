from django.urls import path
from . import views

app_name = "ledger"

urlpatterns = [
    path('', views.index, name="index"),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/list', views.recipe_list, name="recipe_list"),
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
]
