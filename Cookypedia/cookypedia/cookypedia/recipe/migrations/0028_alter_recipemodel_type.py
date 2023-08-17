# Generated by Django 3.2.20 on 2023-08-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0027_alter_recipemodel_recipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='type',
            field=models.CharField(choices=[('-------', 'MAKE_YOUR_CHOICE'), ('Starter', 'STARTER'), ('Main', 'MAIN'), ('Dessert', 'DESSERT')], max_length=7),
        ),
    ]