# Generated by Django 3.2.20 on 2023-08-06 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_rename_recipe_recipemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipemodel',
            old_name='personal_recipe_photo',
            new_name='recipe_photo',
        ),
    ]
