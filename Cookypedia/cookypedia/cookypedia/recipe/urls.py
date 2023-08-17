from django.urls import path, include

from cookypedia.recipe.views import recipe_add, recipe_details, recipe_edit, recipe_delete, other_recipe_details

urlpatterns = (
    path('add/recipe/', recipe_add, name='recipe add'),
    path('<int:pk>/', include([
        path('details/recipe/', recipe_details, name='recipe details'),
        path('other/recipe/', other_recipe_details, name='other recipe details'),
        path('edit/recipe/', recipe_edit, name='recipe edit'),
        path('delete/recipe/', recipe_delete, name='recipe delete'), ]
    ))
)
