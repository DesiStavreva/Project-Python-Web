from django import forms

from cookypedia.cocktail.models import CocktailModel


class BaseForm(forms.ModelForm):
    class Meta:
        model = CocktailModel
        fields = ['name', 'cocktail_photo', 'type', 'ingredients', 'method', ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Cocktail name',
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
            'name': 'Cocktail name',
            'cocktail_photo': 'Photo of the cocktail',
            'type': 'Type of cocktail',
            'ingredients': 'Ingredients',
            'method': 'Method of preparation',
        }


class CocktailAddForm(BaseForm):
    pass


class CocktailEditForm(BaseForm):
    pass
