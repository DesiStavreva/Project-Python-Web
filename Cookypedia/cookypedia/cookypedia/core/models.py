from django.contrib.auth import get_user_model
from django.db import models

from cookypedia.cocktail.models import CocktailModel
from cookypedia.recipe.models import RecipeModel

UserModel = get_user_model()


class RecipeComment(models.Model):
    comment_text = models.TextField(max_length=300, blank=False, null=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ('-date_time_of_publication',)


class CocktailComment(models.Model):
    comment_text = models.TextField(max_length=200, blank=False, null=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_cocktail = models.ForeignKey(CocktailModel, on_delete=models.CASCADE, )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ('-date_time_of_publication',)
