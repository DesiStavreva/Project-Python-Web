# Generated by Django 3.2.20 on 2023-08-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0011_alter_recipemodel_recipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipemodel',
            name='recipe_photo',
            field=models.ImageField(default=5, upload_to=''),
            preserve_default=False,
        ),
    ]
