from django import forms

from cookypedia.recipe.models import RecipeModel, Type


class BaseForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = ['name', 'recipe_photo', 'type', 'ingredients', 'cook_time', 'method', ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Recipe name',
                }
            ),
            'ingredients': forms.TextInput(
                attrs={
                    'placeholder': 'Necessary ingredients',
                }
            ),
            'method': forms.TextInput(
                attrs={
                    'placeholder': 'Method of preparation',
                }
            )
        }
        labels = {
            'name': 'Recipe name',
            'recipe_photo': 'Photo of the dish',
            'type': 'Type of dish',
            'ingredients': 'Ingredients',
            'cook_time': 'Cook time (minutes)',
            'method': 'Method of preparation',
        }


class RecipeAddForm(BaseForm):
    pass


class RecipeEditForm(BaseForm):
    pass


class SearchRecipeForm(forms.Form):
    type = forms.ChoiceField(
        choices=Type.choices(),
        required=False,
    )
