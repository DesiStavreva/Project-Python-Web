from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cookypedia.cocktail.forms import SearchCocktailForm
from cookypedia.cocktail.models import CocktailModel
from cookypedia.core.forms import RecipeCommentForm, CocktailCommentForm
from cookypedia.profiles.models import CustomUser
from cookypedia.recipe.forms import SearchRecipeForm
from cookypedia.recipe.models import RecipeModel


def index(request):

    return render(request, 'core/index.html')


def cookbook(request):
    profile = CustomUser
    recipes = request.user.recipemodel_set.all()
    context = {
        'profile': profile,
        'recipes': recipes,
    }
    return render(request, 'core/cookbook.html', context)


def cocktailbook(request):
    profile = CustomUser
    cocktails = request.user.cocktailmodel_set.all()
    context = {
        'profile': profile,
        'cocktails': cocktails,
    }

    return render(request, 'core/cocktailbook.html', context)


def all_recipes(request):
    recipes = RecipeModel.objects.all()
    comment_form_recipe = RecipeCommentForm()

    search_form_recipe = SearchRecipeForm(request.GET)
    search_pattern = None

    if search_form_recipe.is_valid():
        search_pattern = search_form_recipe.cleaned_data['type']

    if search_pattern:
        recipes = recipes.filter(type__icontains=search_pattern)

    context = {
        'recipes': recipes,
        'comment_form_recipe': comment_form_recipe,
        'search_form_recipe': SearchRecipeForm(),
    }
    return render(request, 'core/all_recipes.html', context)


def all_cocktails(request):
    cocktails = CocktailModel.objects.all()
    comment_form_cocktail = CocktailCommentForm()

    search_form_cocktail = SearchCocktailForm(request.GET)
    search_pattern = None

    if search_form_cocktail.is_valid():
        search_pattern = search_form_cocktail.cleaned_data['type']

    if search_pattern:
        cocktails = cocktails.filter(type__icontains=search_pattern)

    context = {
        'cocktails': cocktails,
        'comment_form_cocktail': comment_form_cocktail,
        'search_form_cocktail': SearchCocktailForm()
    }
    return render(request, 'core/all_cocktails.html', context)


@login_required
def recipe_comment(request, recipe_id):
    recipe = RecipeModel.objects.get(pk=recipe_id)

    if request.method == 'POST':
        form = RecipeCommentForm(request.POST)
        if form.is_valid():
            new_comment_instance = form.save(commit=False)
            new_comment_instance.to_recipe = recipe
            new_comment_instance.user = request.user

            new_comment_instance.save()

        return redirect('all recipes')


@login_required
def cocktail_comment(request, cocktail_id):
    cocktail = CocktailModel.objects.get(pk=cocktail_id)

    if request.method == 'POST':
        form = CocktailCommentForm(request.POST)
        if form.is_valid():
            new_comment_instance = form.save(commit=False)
            new_comment_instance.to_cocktail = cocktail
            new_comment_instance.user = request.user

            new_comment_instance.save()

        return redirect('all cocktails')
