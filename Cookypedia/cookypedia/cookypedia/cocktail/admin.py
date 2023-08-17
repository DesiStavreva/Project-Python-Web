from django.contrib import admin

from cookypedia.cocktail.models import CocktailModel


@admin.register(CocktailModel)
class CocktailAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'cocktail_photo',)


