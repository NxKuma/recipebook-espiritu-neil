from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Recipe, RecipeIngredient

def recipes(request):
    recipe = Recipe.objects.all()
    ctx = { "recipes": recipe}
    return render(request, "recipes.html", ctx)

def recipe(request):
    ingredients = RecipeIngredient.objects.filter(recipe__recipe__name=Recipe.recipe.str)
    ctx = { "ingredients": ingredients}
    return render(request, "recipe.html", ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes.html"    


class IngredientsListView(ListView):
    model = RecipeIngredient
    template_name = "recipe.html"