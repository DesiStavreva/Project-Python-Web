from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cookypedia.cocktail.forms import CocktailAddForm, CocktailEditForm
from cookypedia.cocktail.models import CocktailModel


@login_required
def cocktail_add(request):
    form = CocktailAddForm()

    if request.method == 'POST':
        form = CocktailAddForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            return redirect('cocktailbook')

    context = {
        "form": form,
    }

    return render(request, 'cocktail/cocktail-add.html', context=context)


@login_required
def cocktail_details(request, pk):
    cocktail = CocktailModel.objects.get(pk=pk)

    context = {
        'cocktail': cocktail,
    }

    return render(request, 'cocktail/cocktail-details.html', context)


@login_required
def other_cocktail_details(request, pk):
    cocktail = CocktailModel.objects.get(pk=pk)

    context = {
        'cocktail': cocktail,
    }

    return render(request, 'cocktail/other-cocktail-details.html', context)


@login_required
def cocktail_edit(request, pk):
    cocktail = CocktailModel.objects.get(pk=pk)
    form = CocktailEditForm(instance=cocktail)

    if request.method == "POST":
        form = CocktailEditForm(request.POST, instance=cocktail)
        if form.is_valid():
            recipe = form.save(commit=False)
            cocktail.cocktail_photo = request.FILES.get('cocktail_photo')
            cocktail.save()
            return redirect('cocktail details', pk=pk)

    context = {
        "cocktail": cocktail,
        "form": form,
    }

    return render(request, 'cocktail/cocktail-edit.html', context)


@login_required
def cocktail_delete(request, pk):
    cocktail = CocktailModel.objects.get(pk=pk)
    cocktail.delete()
    return redirect('cocktailbook')
