from django.contrib import admin

from cookypedia.recipe.models import RecipeModel


@admin.register(RecipeModel)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'recipe_photo',)


