from django.contrib import admin

from .models import Recipe, RecipeIngredient, Ingredient

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline,  ]


admin.site.register(Recipe, RecipeAdmin)

