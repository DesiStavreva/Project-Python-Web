from django.contrib import admin

from cookypedia.recipe.models import RecipeModel


@admin.register(RecipeModel)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'recipe_photo', 'type', 'cook_time')
    list_per_page = 10
    list_filter = ('type', 'cook_time')

