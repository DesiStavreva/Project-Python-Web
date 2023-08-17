from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy

from cookypedia.profiles.models import CustomUser
from cookypedia.recipe.forms import RecipeAddForm, RecipeEditForm
from cookypedia.recipe.models import RecipeModel

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as views

UserModel = get_user_model()


@login_required
def recipe_add(request):
    form = RecipeAddForm()

    if request.method == 'POST':
        form = RecipeAddForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            return redirect('cookbook')

    context = {
        "form": form,
    }

    return render(request, 'recipe/recipe-add.html', context=context)


@login_required
def recipe_details(request, pk):
    recipe = RecipeModel.objects.get(pk=pk)

    context = {
        'recipe': recipe,
    }

    return render(request, 'recipe/recipe-details.html', context)


@login_required
def other_recipe_details(request, pk):
    recipe = RecipeModel.objects.get(pk=pk)

    context = {
        'recipe': recipe,
    }

    return render(request, 'recipe/other-recipe-details.html', context)


@login_required
def recipe_edit(request, pk):
    recipe = RecipeModel.objects.get(pk=pk)
    form = RecipeEditForm(instance=recipe)

    if request.method == "POST":
        form = RecipeEditForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.recipe_photo = request.FILES.get('recipe_photo')
            recipe.save()
            return redirect('recipe details', pk=pk)

    context = {
        "recipe": recipe,
        "form": form,
    }

    return render(request, 'recipe/recipe-edit.html', context)


@login_required
def recipe_delete(request, pk):
    recipe = RecipeModel.objects.get(pk=pk)
    recipe.delete()
    return redirect('cookbook')
