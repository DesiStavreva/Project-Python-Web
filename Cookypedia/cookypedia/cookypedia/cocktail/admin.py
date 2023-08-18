from django.contrib import admin

from cookypedia.cocktail.models import CocktailModel


@admin.register(CocktailModel)
class CocktailModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'cocktail_photo', 'type')
    list_per_page = 10
    list_filter = ('type',)