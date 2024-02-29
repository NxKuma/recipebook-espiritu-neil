from django.urls import path
from .views import recipe, RecipeListView, IngredientsListView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>', IngredientsListView.as_view(), name='ingredient-detail'),
]

app_name = "ledger"