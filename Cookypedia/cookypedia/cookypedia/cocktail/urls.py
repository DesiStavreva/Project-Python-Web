from django.urls import path, include


from cookypedia.cocktail.views import cocktail_add, cocktail_details, cocktail_edit, cocktail_delete, \
    other_cocktail_details

urlpatterns = (path('add/cocktail/', cocktail_add, name='cocktail add'),
               path('<int:pk>/', include([
                   path('details/cocktail/', cocktail_details, name='cocktail details'),
                   path('other/cocktail/', other_cocktail_details, name='other cocktail details'),
                   path('edit/cocktail/', cocktail_edit, name='cocktail edit'),
                   path('delete/cocktail/', cocktail_delete, name='cocktail delete'), ]
               )))
