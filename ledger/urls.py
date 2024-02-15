from django.urls import path
from .views import recipe, recipes_1, recipes_2

urlpatterns = [
    path('recipes/list', recipe, name='recipe_list'),
    path('recipe/1', recipes_1, name='recipe_1'),
    path('recipe/2', recipes_2, name='recipe_2'),
]

app_name = "ledger"