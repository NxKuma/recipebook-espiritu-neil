from django.urls import path
from .views import recipe, recipes_1, recipes_2

urlpatterns = [
    path('recipes/list', recipe, name='Recipe_List'),
    path('recipe/1', recipes_1, name='Recipe_1'),
    path('recipe/2', recipes_2, name='Recipe_2'),
]

app_name = "ledger"