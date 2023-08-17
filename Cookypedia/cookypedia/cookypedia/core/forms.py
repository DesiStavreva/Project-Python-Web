from django import forms

from cookypedia.core.models import RecipeComment, CocktailComment


class RecipeCommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...',
                })
        }


class CocktailCommentForm(forms.ModelForm):
    class Meta:
        model = CocktailComment
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...',
                })
        }

