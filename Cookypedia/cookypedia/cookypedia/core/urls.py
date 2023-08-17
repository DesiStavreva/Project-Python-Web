from django.urls import path

from cookypedia.core.views import index, cookbook, cocktailbook, all_recipes, all_cocktails, recipe_comment, \
    cocktail_comment

urlpatterns = (
    path('', index, name='index'),
    path('cookbook/', cookbook, name='cookbook'),
    path('cocktailbook/', cocktailbook, name='cocktailbook'),
    path('all-recipes/', all_recipes, name='all recipes'),
    path('all-cocktails/', all_cocktails, name='all cocktails'),
    path('comment/<int:recipe_id>/', recipe_comment, name='comment recipe'),
    path('comment-/<int:cocktail_id>/', cocktail_comment, name='comment cocktail'),
)
