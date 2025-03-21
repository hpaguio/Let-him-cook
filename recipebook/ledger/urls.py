from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/list', views.recipe_list, name="recipe_list"),
    path('login/', auth_views.LoginView.as_view(template_name='ledger/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

app_name = "ledger"